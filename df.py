import subprocess, sys, time, os

env = os.environ.copy()  # keep your venv
api = subprocess.Popen([sys.executable, "-m", "uvicorn", "app:app", "--reload", "--port", "8000"], env=env)
try:
    time.sleep(2)  # tiny wait for API to start
    subprocess.run([sys.executable, "-m", "streamlit", "run", "frontend.py"], env=env, check=True)
finally:
    api.terminate()
