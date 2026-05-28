$wikiDir = Join-Path $PWD.Path "wiki"
$mdFiles = Get-ChildItem -Path $wikiDir -Recurse -Filter "*.md"
$brokenLinks = 0

Write-Host "Starting Lint: Checking all Markdown links in WikiLLM..."

foreach ($file in $mdFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    if (-not $content) { continue }
    
    # 匹配 Markdown 連結 [text](url)
    $matches = [regex]::Matches($content, '\[.*?\]\((.*?)\)')
    foreach ($m in $matches) {
        $link = $m.Groups[1].Value
        
        # 忽略 http, https, mailto, file 或是純頁內錨點 #
        if ($link -match "^http" -or $link -match "^mailto" -or $link -match "^#" -or $link -match "^file:" -or $link -match "^<") {
            continue
        }
        
        # 處理包含 # 的路徑，如 path/to/file.md#header
        $linkPath = $link -replace '#.*$', ''
        if ([string]::IsNullOrWhiteSpace($linkPath)) {
            continue
        }

        # 解碼 URL 編碼 (例如 %20 -> 空格)
        $linkPath = [System.Uri]::UnescapeDataString($linkPath)

        $targetPath = Join-Path (Split-Path $file.FullName) $linkPath
        $targetPath = [System.IO.Path]::GetFullPath($targetPath)
        
        if (-not (Test-Path $targetPath -PathType Leaf)) {
            if (-not (Test-Path $targetPath -PathType Container)) {
                Write-Host "BROKEN LINK in $($file.Name): $link"
                Write-Host "  -> Target not found: $targetPath"
                $brokenLinks++
            }
        }
    }
}

Write-Host "----------------------------------------"
if ($brokenLinks -eq 0) {
    Write-Host "✅ LINT SUCCESS: 0 broken links found. All links are healthy."
} else {
    Write-Host "❌ LINT FAILED: $brokenLinks broken links found."
}
