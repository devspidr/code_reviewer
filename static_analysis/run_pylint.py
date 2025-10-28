# small helper to run pylint programmatically if needed
import subprocess, sys

def run_pylint(path):
    result = subprocess.run([sys.executable, "-m", "pylint", path], capture_output=True, text=True)
    return result.stdout
