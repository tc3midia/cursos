param(
  [string]$Source = 'D:\Cursos\Formato Criativo de Conteúdo',
  [string]$Destination = 'G:\Meu Drive\Biblioteca\formato-criativo-de-conteudo'
)

$ErrorActionPreference = 'Stop'
$modules = @(
  'Módulo 01 - O método Formato Criativo de Conteúdo',
  'Módulo 02 - Formatos validados para copiar e colar',
  'Módulo 03 - Roteiro Simplificado',
  'Módulo 04 - Bastidores de Gravação',
  'Módulo 05 - Autenticidade com estratégia',
  'Módulo 06 - Vender sem ser chato',
  'Módulo 07 - Introdução à profissão Criador Estrategista'
)

$videos = @(Get-ChildItem -LiteralPath $Source -File -Recurse -Filter '*.mkv' | Where-Object {
  $_.Name -match '^m([1-7])_a\d+_.+\.mkv$'
} | Sort-Object Name)
if ($videos.Count -ne 54) { throw "Inventário inesperado: $($videos.Count) vídeos" }

foreach ($video in $videos) {
  $number = [int]([regex]::Match($video.Name, '^m([1-7])_').Groups[1].Value)
  $modulePath = Join-Path $Destination $modules[$number - 1]
  if (-not (Test-Path -LiteralPath $modulePath)) { throw "Pasta não encontrada: $modulePath" }
  $files = @($video.FullName, ($video.FullName + '.json'))
  $support = [System.IO.Path]::ChangeExtension($video.FullName, '.md')
  if (Test-Path -LiteralPath $support) { $files += $support }
  foreach ($path in $files) {
    if (-not (Test-Path -LiteralPath $path)) { throw "Fonte não encontrada: $path" }
    $target = Join-Path $modulePath ([System.IO.Path]::GetFileName($path))
    $sourceLength = (Get-Item -LiteralPath $path).Length
    if (Test-Path -LiteralPath $target) {
      if ((Get-Item -LiteralPath $target).Length -ne $sourceLength) {
        throw "Tamanho divergente no destino: $target"
      }
      continue
    }
    Copy-Item -LiteralPath $path -Destination $target
    if ((Get-Item -LiteralPath $target).Length -ne $sourceLength) {
      throw "Cópia incompleta: $target"
    }
    Write-Output "Copiado: $number/$([System.IO.Path]::GetFileName($path))"
  }
}
