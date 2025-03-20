import subprocess
import sys

def is_pip_available():
    """
    Function to check if pip is available.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Is pip available: {is_pip_available()}")
