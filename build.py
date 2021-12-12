import os
import subprocess

if (os.name == "posix"):
    os.system('python3 -m PyInstaller --onefile --add-data "data/img:." --add-data "src:src" ToolBox.pyw')
elif (os.name == "nt"):
    subprocess.call(r"python -m PyInstaller --onefile --add-data data\\img;. --add-data src;src ToolBox.pyw")
