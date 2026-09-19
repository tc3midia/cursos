param([int]$FirstFinalizerProcessId)

$ErrorActionPreference = 'Stop'
$output = 'D:\Cursos\Hardcopy Pro - Transcrições'
$script = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($FirstFinalizerProcessId -gt 0) {
  Wait-Process -Id $FirstFinalizerProcessId -ErrorAction SilentlyContinue
}
$state = Get-Content -LiteralPath (Join-Path $output 'status.json') -Raw | ConvertFrom-Json
if ($state.videos_total -ne 136 -or $state.videos_complete -ne 136 -or $state.errors.Count -gt 0) {
  throw "Primeiro lote incompleto: $($state.videos_complete)/$($state.videos_total); erros: $($state.errors.Count)"
}
& python (Join-Path $script 'transcrever.py')
if ($LASTEXITCODE -ne 0) { throw 'Falha na transcrição final' }
$state = Get-Content -LiteralPath (Join-Path $output 'status.json') -Raw | ConvertFrom-Json
if ($state.videos_total -ne 138 -or $state.videos_complete -ne 138 -or $state.errors.Count -gt 0) {
  throw "Curso incompleto: $($state.videos_complete)/$($state.videos_total); erros: $($state.errors.Count)"
}
& python (Join-Path $script 'sincronizar_acervo.py')
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar o acervo final' }
& python (Join-Path $script 'validar.py')
if ($LASTEXITCODE -ne 0) { throw 'Falha na validação do acervo final' }
Write-Output 'Lote final 138/138 concluído e validado.'
