import os
import sys

os.chdir(os.path.abspath(os.path.dirname(__file__)))

os.chdir(os.path.abspath("../"))
os.chdir(os.path.abspath("../"))

sys.path.insert(0, os.getcwd())

import globalvars

print("if this errors out dont worry:")
os.system("swww init")
print("============")
print("if anything errors out after now then DO worry")
if os.path.isfile(globalvars.gifwallpaperpath):
    os.system("swww img " + globalvars.gifwallpaperpath)
elif os.path.isfile(globalvars.staticwallpaperpath):
    os.system("swww img " + globalvars.staticwallpaperpath)
