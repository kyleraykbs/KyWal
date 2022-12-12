print("Its Hyprtime bois!")
import sys
import os
import shutil
import subprocess
from customcolors import *
import globalvars

f = open(globalvars.userdir + "/.cache/wal/colors")
colorsraw = f.readlines()
colors = []
for clr in colorsraw:
    colors.append(clr.strip())

def NotSupportedWallpaperMGR():
    print(fg.blue + "WARN: it appears you arent using a supported wallpaper setter")
    print("or it isn't currently running. Currently the only supported wallpaper setters are")
    print("(swww) if you are using one of the supported wallpaper setters make sure that it is configured properly.")
    print("If its an active wallpaper setter make sure the process is running. >then rerun the script<")
    print("")
    print("if you are not using a supported one you can manually reference the wallpaper using")
    print(fg.lightcyan + globalvars.staticwallpaperpath + fg.reset)
    print("")
    input("(press enter to continue)")

# check if we are using a supported wallpaper runner
runningapps = subprocess.getoutput("ps -e")
if " swww" in runningapps:
    print(fg.green + "Supported wallpaper manager detected!")
    print("(swww)" + fg.reset)
    print("")

    runcommand = "python '" + globalvars.swwwextmoddir + "'"

    os.system(runcommand)
    configpath = globalvars.userdir + "/.config/hypr/hyprland.conf"
    configbackup = configpath + ".kywal.bak"
    if os.path.exists(configpath):
        print(fg.green + "Found config file: " + configpath + "!" + fg.reset)
        if os.path.exists(configbackup):
            os.remove(configbackup)
            shutil.copyfile(configpath, configbackup)
        print(fg.cyan + "Backed up " + configpath + " to " + configbackup + fg.reset)
        
        f = open(configpath, "r")
        data = f.read()
        f.close()

        f = open(configpath, "r")
        lines = f.readlines()
        f.close()
        
        newlines = []
        for line in lines:
                if line.strip().startswith("col.active_border"):
                        line = line.split("=")
                        line[1] = "rgba(" + colors[1].replace("#", "") + "ff) rgba(" + colors[2].replace("#", "") + "ff) 45deg"
                        line = "= ".join(line) + "\n"
                newlines.append(line)
        
        if runcommand not in data:
            newlines.append('\nexec=' + runcommand + "\n")

        f = open(configpath, "w")
        f.writelines(newlines)
        f.close()
    else:
        print(fg.red + "ERROR: Config path does not exist: " + configpath + fg.reset)
else:
    NotSupportedWallpaperMGR()
