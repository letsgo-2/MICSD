param(
  [int]$StartBatch = 2,
  [int]$BatchSize = 5
)

$ErrorActionPreference = "Stop"

$Root = "D:\knoewledge alinment\ka-wiki"
$Manifest = Join-Path $Root "source_batches.csv"

Set-Location $Root

if (!(Test-Path $Manifest)) {
  throw "Missing source_batches.csv. Do not run -Initialize again unless you intentionally reset batching."
}

function Approve-PendingCandidates {
  $candidatesDir = Join-Path $Root ".llmwiki\candidates"
  if (!(Test-Path $candidatesDir)) {
    Write-Host "No candidates directory."
    return
  }

  $candidates = Get-ChildItem $candidatesDir -Filter *.json -File | Sort-Object Name
  if ($candidates.Count -eq 0) {
    Write-Host "No pending candidates to approve."
    return
  }

  Write-Host "Approving $($candidates.Count) pending candidates..."
  foreach ($file in $candidates) {
    $id = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    Write-Host "APPROVE $id"
    llmwiki review approve $id
  }
}

$rows = Import-Csv $Manifest
$totalSources = $rows.Count
$totalBatches = [math]::Ceiling($totalSources / $BatchSize)

Write-Host "Total sources in manifest: $totalSources"
Write-Host "Batch size: $BatchSize"
Write-Host "Total batches: $totalBatches"
Write-Host "Starting from batch: $StartBatch"

Approve-PendingCandidates

for ($batch = $StartBatch; $batch -le $totalBatches; $batch++) {
  Write-Host ""
  Write-Host "============================================================"
  Write-Host "Enabling cumulative batch $batch / $totalBatches"
  Write-Host "============================================================"

  & (Join-Path $Root "enable_source_batch.ps1") -BatchNumber $batch -BatchSize $BatchSize

  Write-Host ""
  Write-Host "Compiling batch $batch in review mode..."
  & (Join-Path $Root "compile_ka_wiki_review.ps1")

  Write-Host ""
  Write-Host "Approving candidates produced by batch $batch..."
  Approve-PendingCandidates

  Write-Host ""
  Write-Host "Status after batch ${batch}:"
  llmwiki status --json
}

Write-Host ""
Write-Host "All configured batches completed. Final status:"
llmwiki status --json
