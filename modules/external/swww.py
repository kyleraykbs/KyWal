import os
import sys
import time

time.sleep(1) # give wm time to start

os.chdir(os.path.abspath(os.path.dirname(__file__)))

os.chdir(os.path.abspath("../"))
os.chdir(os.path.abspath("../"))

sys.path.insert(0, os.getcwd())

import globalvars

print("if this errors out dont worry:")
os.system("swww init")
time.sleep(1) # give swww time to init
print("============")
print("if anything errors out after now then DO worry")
if os.path.isfile(globalvars.gifwallpaperpath):
    os.system("swww img " + globalvars.gifwallpaperpath)
elif os.path.isfile(globalvars.staticwallpaperpath):
    os.system("swww img " + globalvars.staticwallpaperpath)
