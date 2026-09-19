param(
  [string]$Source = 'D:\Cursos\Hardcopy Pro',
  [string]$Destination = 'G:\Meu Drive\Biblioteca\hardcopy-pro'
)

$ErrorActionPreference = 'Stop'
$files = @(Get-ChildItem -LiteralPath $Source -Recurse -File)
if ($files.Count -lt 233) { throw "Inventário menor que o observado: $($files.Count) arquivos" }
foreach ($file in $files) {
  $relative = [System.IO.Path]::GetRelativePath($Source, $file.FullName)
  $target = Join-Path $Destination $relative
  $parent = Split-Path -Parent $target
  New-Item -ItemType Directory -Path $parent -Force | Out-Null
  if (Test-Path -LiteralPath $target) {
    if ((Get-Item -LiteralPath $target).Length -ne $file.Length) {
      throw "Tamanho divergente no destino: $relative"
    }
    continue
  }
  Copy-Item -LiteralPath $file.FullName -Destination $target
  if ((Get-Item -LiteralPath $target).Length -ne $file.Length) {
    throw "Cópia incompleta: $relative"
  }
  Write-Output "Copiado: $relative"
}
Write-Output "Cópia local concluída: $($files.Count) arquivos. Aguardar sincronização e conferir pela API."
