# HTML Encoding Validator
# Checks all HTML files for encoding corruption before commit
# Run before: git add . && git commit
# Usage: powershell -File validate-encoding.ps1

$ErrorActionPreference = "Stop"
$base = $PSScriptRoot
if (-not $base) { $base = Split-Path -Parent $MyInvocation.MyCommand.Path }

Write-Host "Checking HTML files for encoding corruption..." -ForegroundColor Yellow

$badFiles = @()
$files = Get-ChildItem -Path $base -Include "*.html","*.css","*.js" -Recurse -File | Where-Object { $_.FullName -notmatch 'node_modules|\.git' }

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    # Check for U+FFFD replacement characters
    if ($content -match '\ufffd') {
        $badFiles += @{
            File = $f.FullName
            Issue = "U+FFFD replacement character found"
        }
    }

    # Check for common mojibake patterns (double-encoded UTF-8 appearing as Latin1)
    if ($content -match '(&#x[A-Fa-f0-9]{4};)|(Ã[A-Za-z])|(â€™)|(â€[œ""''])|(\xc3[\x80-\xbf])') {
        $badFiles += @{
            File = $f.FullName
            Issue = "Possible mojibake/double-encoding detected"
        }
    }

    # Check for HTML entity encoding issues
    $badEntityCount = ([regex]::Matches($content, '&[a-zA-Z]+;|[&][#]')).Count
}

if ($badFiles.Count -gt 0) {
    Write-Host "`nENCODING ERRORS FOUND - Cannot commit!" -ForegroundColor Red
    foreach ($bf in $badFiles) {
        Write-Host "  $($bf.File)" -ForegroundColor Red
        Write-Host "    Issue: $($bf.Issue)" -ForegroundColor DarkYellow
    }
    Write-Host "`nFix encoding issues before committing." -ForegroundColor Red
    exit 1
} else {
    Write-Host "All files passed encoding check. Safe to commit." -ForegroundColor Green
    exit 0
}
