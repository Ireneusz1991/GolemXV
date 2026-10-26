@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Uruchamianie platformy Golem XV — Ludzie: Droga do Rzeczywistosci...
start "" "http://localhost:8080"
where node >nul 2>nul
if %errorlevel%==0 (
    node server.js
) else (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0server.ps1"
)
pause
