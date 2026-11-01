@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Golem XV — Cykliczna Aktualizacja Bazy Wiedzy (Cron)

echo ===============================================================================
echo   GOLEM XV — CYKLICZNA AKTUALIZACJA ZASOBÓW WIEDZY I BADAŃ NAUKOWYCH
echo ===============================================================================
echo.

set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

if not exist "archives" mkdir archives

if exist "%PYTHON_PATH%" (
    "%PYTHON_PATH%" golem_updater.py --cron >> "archives\cron_update.log" 2>&1
    "%PYTHON_PATH%" golem_updater.py --cron
) else (
    python golem_updater.py --cron >> "archives\cron_update.log" 2>&1
    python golem_updater.py --cron
)

echo.
echo [✓] Log operacji zapisany w: archives\cron_update.log
echo [✓] Zmiany zapisano lokalnie w bazie bez tworzenia nowego commita w Git.
echo.
timeout /t 5 >nul
