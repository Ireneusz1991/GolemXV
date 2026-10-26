$ErrorActionPreference = "Stop"
$Port = 8080
$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$DataDir = Join-Path $RootDir "data"
$SeedFile = Join-Path $DataDir "seed.json"
$DbFile = Join-Path $DataDir "database.json"

if (-not (Test-Path $DataDir)) {
    New-Item -ItemType Directory -Path $DataDir | Out-Null
}
if ((-not (Test-Path $DbFile)) -and (Test-Path $SeedFile)) {
    Copy-Item $SeedFile $DbFile
}

$Listener = New-Object System.Net.HttpListener
$Listener.Prefixes.Add("http://localhost:$Port/")
$Listener.Start()

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " Golem XV — Ludzie: Droga do Rzeczywistości (Serwer HTTP)" -ForegroundColor Cyan
Write-Host " Adres aplikacji: http://localhost:$Port" -ForegroundColor Green
Write-Host " Baza danych JSON: $DbFile" -ForegroundColor Gray
Write-Host " Naciśnij Ctrl+C, aby zatrzymać serwer." -ForegroundColor Yellow
Write-Host "============================================================"

try {
    while ($Listener.IsListening) {
        $Context = $Listener.GetContext()
        $Request = $Context.Request
        $Response = $Context.Response
        $Path = $Request.Url.LocalPath

        if ($Path -eq "/api/state" -and $Request.HttpMethod -eq "GET") {
            $Target = if (Test-Path $DbFile) { $DbFile } else { $SeedFile }
            $Bytes = [System.IO.File]::ReadAllBytes($Target)
            $Response.ContentType = "application/json; charset=utf-8"
            $Response.StatusCode = 200
            $Response.OutputStream.Write($Bytes, 0, $Bytes.Length)
            $Response.Close()
            continue
        }

        if ($Path -eq "/api/backup_archive" -and $Request.HttpMethod -eq "POST") {
            $NowStr = (Get-Date).ToUniversalTime().ToString("yyyyMMdd_HHmmss")
            $ArchDir = Join-Path $RootDir "archives"
            if (-not (Test-Path $ArchDir)) { New-Item -ItemType Directory -Path $ArchDir | Out-Null }
            $BakPath = Join-Path $ArchDir "database_backup_$NowStr.json"
            if (Test-Path $DbFile) { Copy-Item $DbFile $BakPath }
            $OkBytes = [System.Text.Encoding]::UTF8.GetBytes("{`"ok`":true,`"file`":`"$BakPath`"}")
            $Response.ContentType = "application/json; charset=utf-8"
            $Response.StatusCode = 200
            $Response.OutputStream.Write($OkBytes, 0, $OkBytes.Length)
            $Response.Close()
            continue
        }

        if ($Path -eq "/api/state" -and $Request.HttpMethod -eq "POST") {
            $Reader = New-Object System.IO.StreamReader($Request.InputStream, [System.Text.Encoding]::UTF8)
            $Body = $Reader.ReadToEnd()
            $Reader.Close()
            [System.IO.File]::WriteAllText($DbFile, $Body, [System.Text.Encoding]::UTF8)
            $OkBytes = [System.Text.Encoding]::UTF8.GetBytes('{"ok":true}')
            $Response.ContentType = "application/json; charset=utf-8"
            $Response.StatusCode = 200
            $Response.OutputStream.Write($OkBytes, 0, $OkBytes.Length)
            $Response.Close()
            continue
        }

        $RelPath = if ($Path -eq "/") { "index.html" } else { $Path.TrimStart('/') }
        $FullPath = Join-Path $RootDir $RelPath

        if (Test-Path $FullPath -PathType Leaf) {
            $Ext = [System.IO.Path]::GetExtension($FullPath).ToLower()
            switch ($Ext) {
                ".html" { $Response.ContentType = "text/html; charset=utf-8" }
                ".css"  { $Response.ContentType = "text/css; charset=utf-8" }
                ".js"   { $Response.ContentType = "application/javascript; charset=utf-8" }
                ".json" { $Response.ContentType = "application/json; charset=utf-8" }
                default { $Response.ContentType = "application/octet-stream" }
            }
            $FileBytes = [System.IO.File]::ReadAllBytes($FullPath)
            $Response.StatusCode = 200
            $Response.OutputStream.Write($FileBytes, 0, $FileBytes.Length)
        } else {
            $Response.StatusCode = 404
        }
        $Response.Close()
    }
} finally {
    $Listener.Stop()
}
