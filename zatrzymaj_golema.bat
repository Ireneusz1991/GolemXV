@echo off
chcp 65001 >nul
title Golem XV — Zatrzymanie Uslugi

echo ===============================================================================
echo   Zatrzymywanie uslug Golem XV i serwera Streamlit...
echo ===============================================================================
echo.

python -c "
import sys, os
sys.path.insert(0, r'%~dp0')
import golem_watchdog
golem_watchdog.kill_processes_on_port(8501)
golem_watchdog.kill_processes_on_port(8080)
golem_watchdog.update_status('STOPPED', 0, '', 'Zatrzymano recznie przez zatrzymaj_golema.bat')
print('[✓] Procesy na portach 8501 i 8080 zostaly pomyslnie zakonczone.')
"

echo.
echo ===============================================================================
echo   Platforma Golem XV zostala zatrzymana.
echo ===============================================================================
timeout /t 3 >nul
