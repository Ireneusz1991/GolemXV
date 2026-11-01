@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Golem XV — Rejestracja Harmonogramu Zadań (Cron)

echo ===============================================================================
echo   INSTALACJA CYKLICZNEGO CRONA GOLEM XV W HARMONOGRAMIE ZADAŃ WINDOWS
echo ===============================================================================
echo.
echo Skrypt skonfiguruje automatyczne zadanie w systemie Windows, które raz dziennie
echo o godzinie 03:00 w nocy (lub przy włączeniu komputera) pobierze najświeższe badania
echo z arXiv, zaktualizuje bazę i wykona kopię bezpieczeństwa — BEZ NOWYCH COMMITÓW.
echo.

set TASK_NAME=GolemXV_Cykliczny_Updater
set BATCH_PATH=%~dp0cron_aktualizacja.bat

schtasks /create /tn "%TASK_NAME%" /tr "\"%BATCH_PATH%\"" /sc daily /st 03:00 /f >nul 2>&1

if %errorlevel%==0 (
    echo [✓] Zadanie "%TASK_NAME%" zostalo pomyslnie zarejestrowane w Harmonogramie Zadan!
    echo [✓] Czestotliwosc: Codziennie o 03:00 (lub przy najblizszym uruchomieniu PC).
) else (
    echo [!] Uwaga: Standardowa proba rejestracji wymaga uprawnien uzytkownika.
    echo     Probuje zarejestrowac zadanie dla biezacego uzytkownika...
    schtasks /create /tn "%TASK_NAME%" /tr "\"%BATCH_PATH%\"" /sc onlogon /f >nul 2>&1
    if %errorlevel%==0 (
        echo [✓] Zarejestrowano zadanie uruchamiane przy kazdym logowaniu do Windowsa!
    ) else (
        echo [!] Nie udalo sie automatycznie dodac do schtasks. Mozesz uruchamiac cron_aktualizacja.bat recznie lub przez autostart.
    )
)

echo.
echo ===============================================================================
echo   Zadanie bedzie dzialac w pelni autonomicznie w tle.
echo ===============================================================================
echo.
pause
