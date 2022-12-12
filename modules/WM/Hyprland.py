print("Its Hyprtime bois!")
import sys
import os
import shutil
import subprocess
from customcolors import *
import globalvars

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

        if runcommand not in data:
            lines.append('\nexec=' + runcommand + "\n")

        f = open(configpath, "w")
        f.writelines(lines)
        f.close()
    else:
        print(fg.red + "ERROR: Config path does not exist: " + configpath + fg.reset)
else:
    NotSupportedWallpaperMGR()
