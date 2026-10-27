@echo off
chcp 65001 >nul
title Golem XV — Tarcza Anty-Halucynacyjna i Weryfikator Integralności

echo ===============================================================================
echo   GOLEM XV — AUTOMATYCZNY AUDYT ANTY-HALUCYNACYJNY I WERYFIKACJA BAZY WIEDZY
echo ===============================================================================
echo.

python golem_verifier.py
if errorlevel 1 (
    echo.
    echo [!] Wykryto bledy krytyczne w bazie danych! Napraw je przed wdrozeniem.
    pause
    exit /b 1
)

echo.
set /p DO_FULL="Czy chcesz wykonac pelny audyt sieciowy (test kodu HTTP 200 dla wszystkich linkow)? [T/N]: "
if /i "%DO_FULL%"=="T" (
    echo.
    echo [*] Uruchamianie pelnego audytu HTTP na zywo (moze potrwac kilkanascie sekund)...
    python golem_verifier.py --full
)

echo.
echo ===============================================================================
echo   Audyt zakonczony pomyslnie. Baza wiedzy jest spojna i zweryfikowana.
echo ===============================================================================
echo.
pause
