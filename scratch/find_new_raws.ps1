$baseDir = $PWD.Path
$rawDir = Join-Path $baseDir "raw"
$wikiSourcesDir = Join-Path $baseDir "wiki\sources"
$outputFile = Join-Path $baseDir "scratch\new_raws_output.txt"

# 1. Get all raw files (excluding dot-files, README.md, assets)
$rawFiles = @()
if (Test-Path $rawDir) {
    $rawFiles = Get-ChildItem -Path $rawDir -Recurse -File | Where-Object {
        $_.Name -notlike ".*" -and $_.Name -ne "README.md" -and $_.FullName -notlike "*\raw\assets\*"
    }
}

# 2. Get ingested sources patterns
$ingestedPatterns = @()
if (Test-Path $wikiSourcesDir) {
    $sources = Get-ChildItem -Path $wikiSourcesDir -Filter "*.md"
    foreach ($s in $sources) {
        $content = Get-Content -Path $s.FullName -Raw -Encoding UTF8
        if ($content -match '(?m)^source_file:\s*["'']?([^"''\r\n]+)["'']?') {
            $srcPath = $Matches[1].Trim()
            $srcPath = $srcPath.Replace("\", "/")
            # Escape regex chars except wildcard *
            $regexPattern = [regex]::Escape($srcPath).Replace('\\\*', '.*')
            $ingestedPatterns += "^" + $regexPattern + "$"
        }
    }
}

# 3. Find un-ingested files
$newFiles = @()
foreach ($f in $rawFiles) {
    $relPath = $f.FullName.Substring($baseDir.Length + 1).Replace("\", "/")
    
    $isIngested = $false
    foreach ($pat in $ingestedPatterns) {
        if ($relPath -match $pat) {
            $isIngested = $true
            break
        }
    }
    
    if (-not $isIngested) {
        $newFiles += $f
    }
}

# 4. Generate report
$report = @()
$report += "=== RECENTLY MODIFIED RAW FILES (Top 20) ==="
$sortedRaw = $rawFiles | Sort-Object LastWriteTime -Descending
$topRaw = $sortedRaw | Select-Object -First 20
foreach ($rf in $topRaw) {
    if ($rf) {
        $rel = $rf.FullName.Substring($baseDir.Length + 1).Replace("\", "/")
        $timeStr = $rf.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")
        $report += "$timeStr | $rel"
    }
}

$report += ""
$report += "=== UN-INGESTED RAW FILES ($($newFiles.Count)) ==="
$sortedNew = $newFiles | Sort-Object FullName
foreach ($nf in $sortedNew) {
    if ($nf) {
        $rel = $nf.FullName.Substring($baseDir.Length + 1).Replace("\", "/")
        $timeStr = $nf.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")
        $report += "$timeStr | $rel"
    }
}

$report | Out-File -FilePath $outputFile -Encoding utf8
Write-Host "Success! Report written to $outputFile"
