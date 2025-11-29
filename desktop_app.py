import os
import sys
import threading
import time
import socket
import webview

# Adjust this to your actual settings module (your project folder name)
DJANGO_SETTINGS_MODULE = 'kb_project.settings'
# Determine project root (when running from source). When frozen by PyInstaller,
# sys.executable is the exe path; we want the dir where the app was installed.
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def start_django_in_thread(host="127.0.0.1", port="8000"):

    def _run():
        if BASE_DIR not in sys.path:
            sys.path.insert(0, BASE_DIR)
        
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
        print(">> Using DJANGO_SETTINGS_MODULE =", os.environ["DJANGO_SETTINGS_MODULE"])
        
        from django.core.management import execute_from_command_line
        try:
            execute_from_command_line([sys.argv[0], "runserver", f"{host}:{int(port)}", "--noreload"])
        except Exception as exc:
            print(">> Django failed to start:", repr(exc))
    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return t
def wait_for_server(host="127.0.0.1", port=8000, timeout=30):
    try:
        port = int(port)
    except (TypeError, ValueError):
        port = 8000

    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except Exception as e:
            print(f"wait_for_server: not up yet: {e!r}")
            time.sleep(0.5)
    return False
def start_app():
    host, port = "127.0.0.1", 8000
    print("Starting Django (in-process)...")
    start_django_in_thread(host, str(port))
    
    print("Waiting for Django to be ready...")
    if wait_for_server(host, port, timeout=30):
        print("Django is up — launching webview")
        webview.create_window("Structured Notes App", f"http://{host}:{port}", width=1200, height=800)
        webview.start()
    else:
        print("ERROR: Django did not start within timeout. Check logs in terminal.")

if __name__ == "__main__":
    start_app()