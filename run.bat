@echo off
title Golem XV — Ludzie: Droga do Rzeczywistosci
chcp 65001 > nul
cd /d "%~dp0"

echo ===============================================================================
echo   Uruchamianie platformy Golem XV z aktywnym strażnikiem ciągłości nadawania
echo ===============================================================================
echo.

set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

if exist "golem_watchdog.py" (
    if exist "%PYTHON_PATH%" (
        "%PYTHON_PATH%" golem_watchdog.py
    ) else (
        python golem_watchdog.py
    )
) else (
    :restart_loop
    echo [*] Uruchamianie Streamlit na porcie 8501...
    if exist "%PYTHON_PATH%" (
        "%PYTHON_PATH%" -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
    ) else (
        python -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
    )
    echo [!] Serwer zakonczyl dzialanie. Automatyczne wznowienie za 3 sekundy...
    timeout /t 3 >nul
    goto restart_loop
)

pause
