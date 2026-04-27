import subprocess
import sys
import os

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
script_path = os.path.join(base_path, "dashboard_v2.py")

subprocess.run([
    sys.executable, "-m", "streamlit", "run", script_path
])