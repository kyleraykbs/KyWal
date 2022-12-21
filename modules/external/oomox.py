import os
import sys

os.chdir(os.path.abspath(os.path.dirname(__file__)))

os.chdir(os.path.abspath("../"))
os.chdir(os.path.abspath("../"))

sys.path.insert(0, os.getcwd())

import globalvars

f = open(os.path.expanduser("~") + "/.cache/wal/colors")
colorsraw = f.readlines()
colors = []
for clr in colorsraw:
    colors.append(clr.strip().replace("#", ""))

papiruspath = "/opt/oomox/plugins/icons_papirus/change_color.sh"
papiruscommand = papiruspath + " -o papirus -c " + colors[1] 

if os.path.exists(papiruspath):
    os.system(papiruscommand)