@echo off
title Golem XV — Ludzie: Droga do Rzeczywistosci
chcp 65001 > nul
echo ========================================================
echo   Uruchamianie platformy Golem XV (Streamlit)
echo ========================================================
echo.

set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

if not exist "%PYTHON_PATH%" (
    python -m streamlit run app.py
) else (
    "%PYTHON_PATH%" -m streamlit run app.py
)

pause
