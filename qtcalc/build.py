import os
from __init__ import __version__

os.system("pyinstaller app.py --onefile --noconsole --icon qtcalc.ico")
os.system(f"mv dist/app.exe dist/qtcalc{__version__}.exe")
