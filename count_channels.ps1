$dir = "c:\Users\alexc\OneDrive\文件\WikiLLM\WikiLLM\raw\BZSdata\SaaS"
$files = Get-ChildItem -Path $dir -Filter "2*.md" | Sort-Object Name
$counts = @{}
$total = 0
foreach ($f in $files) {
    $lines = Get-Content $f.FullName -Encoding UTF8
    foreach ($line in $lines) {
        if ($line -match u'來源管道') {
            if ($line -match u'：(.*)$') {
                $val = $matches[1].Trim()
                if ($val -eq '') { $val = "(空白)" }
                if ($counts.ContainsKey($val)) { $counts[$val]++ } else { $counts[$val] = 1 }
                $total++
            }
        }
    }
}
Write-Host "=== 各管道統計（共 $total 筆） ==="
$counts.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
    Write-Host ("{0,-60} : {1}" -f $_.Key, $_.Value)
}
