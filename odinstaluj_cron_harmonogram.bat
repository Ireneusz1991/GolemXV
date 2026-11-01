@echo off
chcp 65001 >nul
title Golem XV — Usuniecie Harmonogramu Zadan (Cron)

echo ===============================================================================
echo   Usuwanie zadania Golem XV z Harmonogramu Zadan Windows...
echo ===============================================================================
echo.

schtasks /delete /tn "GolemXV_Cykliczny_Updater" /f >nul 2>&1
if %errorlevel%==0 (
    echo [✓] Zadanie GolemXV_Cykliczny_Updater zostalo usuniete.
) else (
    echo [i] Zadanie nie bylo zarejestrowane lub zostalo juz wczesniej usuniete.
)

echo.
pause
