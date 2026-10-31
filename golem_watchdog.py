# -*- coding: utf-8 -*-
"""
Golem XV — Strażnik Ciągłości Działania i Samonaprawczy Watchdog (golem_watchdog.py)
===================================================================================
Zapewnia nieprzerwane nadawanie platformy Golem XV (Streamlit):
- Monitoruje stan zdrowia serwera (endpoint /_stcore/health)
- W razie awarii, zamknięcia okna lub restartu automatycznie wznawia proces w < 5 sekund
- Wykrywa lokalne IP Wi-Fi (192.168.x.x) dla tabletów, smartfonów i odsłuchu w samochodzie
- Zapisuje status i czas pracy (uptime) do pliku data/golem_watchdog_status.json
"""

import os
import sys
import time
import socket
import json
import subprocess
import urllib.request
import signal
from datetime import datetime

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
APP_FILE = os.path.join(WORKSPACE, "app.py")
STATUS_FILE = os.path.join(WORKSPACE, "data", "golem_watchdog_status.json")
STREAMLIT_PORT = 8501
HEALTH_URL = f"http://localhost:{STREAMLIT_PORT}/_stcore/health"
CHECK_INTERVAL_SEC = 8

def get_local_ip() -> str:
    """Wykrywa lokalny adres IP w sieci domowej/Wi-Fi."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1.0)
        # Połączenie pozorne (nie wysyła pakietów w sieć) do ustalenia interfejsu wyjściowego
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def is_server_healthy(timeout: float = 3.0) -> bool:
    """Sprawdza czy Streamlit odpowiada kodem HTTP 200 na endpoincie health."""
    try:
        req = urllib.request.Request(HEALTH_URL, headers={"User-Agent": "GolemWatchdog/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.getcode() == 200
    except Exception:
        return False

def find_process_on_port(port: int):
    """Zwraca listę PID procesów nasłuchujących na danym porcie na Windowsie."""
    pids = []
    try:
        out = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True).decode("ascii", errors="ignore")
        for line in out.strip().splitlines():
            parts = line.split()
            if len(parts) >= 5 and "LISTENING" in parts:
                pid = int(parts[-1])
                if pid not in pids and pid != 0:
                    pids.append(pid)
    except Exception:
        pass
    return pids

def kill_processes_on_port(port: int):
    """Usuwa zawieszone procesy blokujące port."""
    pids = find_process_on_port(port)
    current_pid = os.getpid()
    for pid in pids:
        if pid != current_pid:
            try:
                subprocess.run(f"taskkill /F /PID {pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

def update_status(status: str, restart_count: int, started_at: str, error_msg: str = ""):
    """Zapisuje bieżący stan do pliku JSON."""
    local_ip = get_local_ip()
    payload = {
        "status": status,
        "lastHeartbeat": datetime.now().isoformat(),
        "startedAt": started_at,
        "restartCount": restart_count,
        "localIp": local_ip,
        "localUrl": f"http://localhost:{STREAMLIT_PORT}",
        "networkUrl": f"http://{local_ip}:{STREAMLIT_PORT}",
        "lastError": error_msg
    }
    try:
        os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
        with open(STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

def launch_streamlit() -> subprocess.Popen:
    """Uruchamia proces Streamlit ze zoptymalizowanymi flagami sieciowymi."""
    python_exe = sys.executable
    cmd = [
        python_exe,
        "-m", "streamlit", "run", APP_FILE,
        "--server.port", str(STREAMLIT_PORT),
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false",
        "--browser.gatherUsageStats", "false"
    ]
    # Na Windows uruchamiamy w nowej grupie procesów
    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NEW_PROCESS_GROUP

    proc = subprocess.Popen(
        cmd,
        cwd=WORKSPACE,
        creationflags=creationflags,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return proc

def run_watchdog():
    """Główna pętla samonaprawcza Watchdoga."""
    sys.stdout.reconfigure(encoding="utf-8")
    local_ip = get_local_ip()
    started_at = datetime.now().isoformat()
    restart_count = 0

    print("=" * 76)
    print(" 🛡️  GOLEM XV — STRAŻNIK CIĄGŁOŚCI NADANIA (SAMONAPRAWCZY WATCHDOG)")
    print("=" * 76)
    print(f" * Katalog projektu:  {WORKSPACE}")
    print(f" * Dostęp lokalny:    http://localhost:{STREAMLIT_PORT}")
    print(f" * Sieć Wi-Fi / Auto: http://{local_ip}:{STREAMLIT_PORT}")
    print(f" * Monitorowany port: {STREAMLIT_PORT}")
    print(f" * Interwał kontroli: co {CHECK_INTERVAL_SEC} sekund")
    print("-" * 76)

    # Sprawdzenie wstępne
    if is_server_healthy():
        print("[✓] Serwer Streamlit już działa i odpowiada poprawnie.")
        current_proc = None
    else:
        print("[!] Serwer nie odpowiada. Inicjalizacja pierwszego uruchomienia...")
        kill_processes_on_port(STREAMLIT_PORT)
        current_proc = launch_streamlit()
        time.sleep(3)
        restart_count += 1

    consecutive_failures = 0

    def sig_handler(sig, frame):
        print("\n[*] Zatrzymywanie strażnika Golem XV...")
        update_status("STOPPED", restart_count, started_at)
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, sig_handler)

    print("[*] Strażnik czuwa w tle. Wciśnij Ctrl+C, aby przerwać monitorowanie.")
    print("-" * 76)

    while True:
        try:
            healthy = is_server_healthy()
            if healthy:
                consecutive_failures = 0
                update_status("ONLINE", restart_count, started_at)
            else:
                consecutive_failures += 1
                now_str = datetime.now().strftime("%H:%M:%S")
                print(f"[{now_str}] ⚠️ Brak odpowiedzi od serwera (próba {consecutive_failures}/2)...")

                if consecutive_failures >= 2:
                    print(f"[{now_str}] 🔴 Awaria wykryta! Automatyczne wznawianie procesu Streamlit...")
                    kill_processes_on_port(STREAMLIT_PORT)
                    current_proc = launch_streamlit()
                    restart_count += 1
                    update_status("RESTARTING", restart_count, started_at, "Serwer przestał odpowiadać — wznowiono.")
                    time.sleep(4)
                    if is_server_healthy():
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Serwer pomyślnie przywrócony do życia! (Wznowień łącznie: {restart_count})")
                        consecutive_failures = 0
                    else:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] ⏳ Serwer jeszcze wstaje, oczekiwanie...")

            time.sleep(CHECK_INTERVAL_SEC)
        except Exception as e:
            time.sleep(CHECK_INTERVAL_SEC)

if __name__ == "__main__":
    if "--check" in sys.argv:
        healthy = is_server_healthy()
        ip = get_local_ip()
        print(f"Status: {'ONLINE' if healthy else 'OFFLINE'}")
        print(f"Local URL: http://localhost:{STREAMLIT_PORT}")
        print(f"Network URL: http://{ip}:{STREAMLIT_PORT}")
        sys.exit(0 if healthy else 1)
    elif "--restart" in sys.argv:
        print("[*] Wymuszony restart serwera Streamlit...")
        kill_processes_on_port(STREAMLIT_PORT)
        launch_streamlit()
        time.sleep(3)
        healthy = is_server_healthy()
        print(f"Status po restarcie: {'ONLINE' if healthy else 'FAILED'}")
        sys.exit(0 if healthy else 1)
    else:
        run_watchdog()
