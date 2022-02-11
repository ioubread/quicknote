from pathlib import Path
import pyperclip
import sys, os

desktopDir = Path.home() / 'Desktop'
allArgs = ' '.join(sys.argv[1:])
fileName = (allArgs) + '.txt'

os.chdir(desktopDir)

if not os.path.exists(fileName):
    fileobj = open(fileName, 'w')
    fileobj.write(str(pyperclip.paste()))
    fileobj.close()
