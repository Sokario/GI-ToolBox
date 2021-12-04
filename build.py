import os
import subprocess

if (os.name == "posix"):
    os.system("python3 -m PyInstaller --onefile ToolBox.pyw")
elif (os.name == "nt"):
    subprocess.call(r"python -m PyInstaller --onefile ToolBox.pyw")
