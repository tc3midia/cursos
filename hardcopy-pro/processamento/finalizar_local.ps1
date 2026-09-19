param([int]$TranscriptionProcessId)

$ErrorActionPreference = 'Stop'
$output = 'D:\Cursos\Hardcopy Pro - Transcrições'
$script = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($TranscriptionProcessId -gt 0) {
  Wait-Process -Id $TranscriptionProcessId -ErrorAction SilentlyContinue
}
$state = Get-Content -LiteralPath (Join-Path $output 'status.json') -Raw | ConvertFrom-Json
if ($state.videos_total -ne 113 -or $state.videos_complete -ne 113 -or $state.errors.Count -gt 0) {
  throw "Lote incompleto: $($state.videos_complete)/$($state.videos_total); erros: $($state.errors.Count)"
}
& python (Join-Path $script 'sincronizar_acervo.py')
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar o acervo de texto' }
Write-Output 'Finalização local concluída.'
