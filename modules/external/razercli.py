import os
import sys, time

os.chdir(os.path.abspath(os.path.dirname(__file__)))

os.chdir(os.path.abspath("../"))
os.chdir(os.path.abspath("../"))

sys.path.insert(0, os.getcwd())

import globalvars

f = open(globalvars.userdir + "/.cache/wal/colors")
colorsraw = f.readlines()
colors = []
for clr in colorsraw:
    colors.append(clr.strip().replace("#", ""))
os.system("razer-cli -c FF0000")
time.sleep(1)
os.system(globalvars.razercli + " -e multicolor,6 -c " + colors[1] + " " + colors[2] + " " + colors[3] + " " + colors[4] + " " + colors[5] + " " + colors[6])
