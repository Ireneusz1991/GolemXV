@echo off
chcp 65001 >nul
title Golem XV — Usuniecie Autostartu Windows

echo ===============================================================================
echo   Usuwanie Autostartu Golem XV z folderu startowego Windows...
echo ===============================================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$startup = [Environment]::GetFolderPath('Startup'); " ^
    "$lnkPath = Join-Path $startup 'GolemXV_Autostart.lnk'; " ^
    "if (Test-Path $lnkPath) { Remove-Item $lnkPath -Force; Write-Host '[✓] Skrót GolemXV_Autostart.lnk został usunięty.' } else { Write-Host '[i] Brak zarejestrowanego autostartu.' }"

echo.
pause
