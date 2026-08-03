param(
  [Parameter(Mandatory = $true)]
  [int]$BatchNumber,

  [int]$BatchSize = 5,

  [switch]$Initialize
)

$ErrorActionPreference = "Stop"

$Root = "D:\knoewledge alinment\ka-wiki"
$Sources = Join-Path $Root "sources"
$Hold = Join-Path $Root "sources_disabled"
$Manifest = Join-Path $Root "source_batches.csv"
$State = Join-Path $Root ".llmwiki\state.json"

Set-Location $Root

if ($BatchNumber -lt 1) {
  throw "BatchNumber must be >= 1."
}

if ($Initialize) {
  if (Test-Path $State) {
    throw "Refusing to initialize because .llmwiki\state.json already exists. This batching script is for the first successful compile."
  }

  New-Item -ItemType Directory -Force -Path $Hold | Out-Null

  $allSources = Get-ChildItem -Path $Sources -Filter *.md -File | Sort-Object Name
  if ($allSources.Count -eq 0) {
    throw "No .md source files found in $Sources."
  }

  $rows = for ($i = 0; $i -lt $allSources.Count; $i++) {
    [pscustomobject]@{
      Index = $i + 1
      Batch = [math]::Floor($i / $BatchSize) + 1
      Name = $allSources[$i].Name
    }
  }
  $rows | Export-Csv -Path $Manifest -NoTypeInformation -Encoding UTF8

  foreach ($file in $allSources) {
    Move-Item -LiteralPath $file.FullName -Destination (Join-Path $Hold $file.Name)
  }
}

if (!(Test-Path $Manifest)) {
  throw "Missing $Manifest. Run with -Initialize first."
}

New-Item -ItemType Directory -Force -Path $Sources | Out-Null
New-Item -ItemType Directory -Force -Path $Hold | Out-Null

$rows = Import-Csv $Manifest
$target = $BatchNumber * $BatchSize
$toEnable = $rows | Where-Object { [int]$_.Index -le $target } | Sort-Object {[int]$_.Index}

foreach ($row in $toEnable) {
  $held = Join-Path $Hold $row.Name
  $active = Join-Path $Sources $row.Name
  if ((Test-Path $held) -and !(Test-Path $active)) {
    Move-Item -LiteralPath $held -Destination $active
  }
}

$activeCount = @(Get-ChildItem -Path $Sources -Filter *.md -File).Count
$heldCount = @(Get-ChildItem -Path $Hold -Filter *.md -File).Count

Write-Host "Enabled cumulative batch $BatchNumber with batch size $BatchSize."
Write-Host "Active sources: $activeCount"
Write-Host "Disabled sources: $heldCount"
Write-Host "Next command:"
Write-Host '  & "D:\knoewledge alinment\ka-wiki\compile_ka_wiki.ps1"'
