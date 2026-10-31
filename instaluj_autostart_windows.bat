@echo off
chcp 65001 >nul
title Golem XV — Instalacja Autostartu Windows

echo ===============================================================================
echo   Instalacja Autostartu Golem XV (Uruchamianie w tle przy starcie systemu)
echo ===============================================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$ws = New-Object -ComObject WScript.Shell; " ^
    "$startup = [Environment]::GetFolderPath('Startup'); " ^
    "$lnk = $ws.CreateShortcut((Join-Path $startup 'GolemXV_Autostart.lnk')); " ^
    "$lnk.TargetPath = 'wscript.exe'; " ^
    "$vbsPath = Join-Path '%~dp0' 'uruchom_w_tle.vbs'; " ^
    "$lnk.Arguments = '\"' + $vbsPath + '\"'; " ^
    "$lnk.WorkingDirectory = '%~dp0'; " ^
    "$lnk.Description = 'Automatyczny strażnik Golem XV w tle'; " ^
    "$lnk.Save(); " ^
    "Write-Host '[✓] Skrót autostartu utworzony pomyślnie w: ' $startup"

echo.
echo ===============================================================================
echo   Autostart zostal zainstalowany!
echo   Od teraz przy kazdym logowaniu do Windowsa Golem XV wlaczy sie w tle.
echo ===============================================================================
echo.
pause
