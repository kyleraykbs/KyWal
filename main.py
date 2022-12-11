import install
import globalvars
import sys
import os
import subprocess
from customcolors import *

os.chdir(os.path.abspath(os.path.dirname(__file__)))

if not install.checkForDependancies():
    print(fg.red + "ERROR: Some dependancies could not be found please install them with the instructions on the github!")
    print(fg.reset + globalvars.githublink)
    exit()

def xiwaltopywal(): # this whole function is some code from a previous itteration that i didnt put much effort into probably could use a rework
    output = subprocess.check_output([globalvars.xiwalpath, '-i', globalvars.staticwallpaperpath]).decode('utf-8')
    colors = output.split("#")
    colors[16] = colors[16][0:6]
    colors.reverse()
    colors.pop()
    colors.reverse()

    colors = ''.join(colors)
    colors = colors.split(";")
    ncolors = []
    for color in colors:
        color = "#" + color
        ncolors.append(color)
    colors = ncolors

    f = open(globalvars.themepath + '.json', "r", encoding='utf-8')
    lines = f.readlines()
    f.close()

    def clrc(st, sw, hv):
        hv = hv.lower()
        if (st.startswith(sw)):
            st = st.split(":")
            st = st[0] + ": \"" + hv
            return st
        return st

    newlines = []
    for line in lines:
        line = clrc(line,'        "background": "',colors[0] + '",\n')
        line = clrc(line,'        "foreground": "',colors[15] + '",\n')
        line = clrc(line,'        "cursor": "',colors[15] + '"\n')
        line = clrc(line,'    "wallpaper": "', globalvars.staticwallpaperpath + '",\n')


        line = clrc(line,'        "color0": "',colors[0] + '",\n')
        line = clrc(line,'        "color1": "',colors[1] + '",\n')
        line = clrc(line,'        "color2": "',colors[2] + '",\n')
        line = clrc(line,'        "color3": "',colors[3] + '",\n')
        line = clrc(line,'        "color4": "',colors[4] + '",\n')
        line = clrc(line,'        "color5": "',colors[5] + '",\n')
        line = clrc(line,'        "color6": "',colors[6] + '",\n')
        line = clrc(line,'        "color7": "',colors[7] + '",\n')
        line = clrc(line,'        "color8": "',colors[8] + '",\n')
        line = clrc(line,'        "color9": "',colors[9] + '",\n')
        line = clrc(line,'        "color10": "',colors[10] + '",\n')
        line = clrc(line,'        "color11": "',colors[11] + '",\n')
        line = clrc(line,'        "color12": "',colors[12] + '",\n')
        line = clrc(line,'        "color13": "',colors[13] + '",\n')
        line = clrc(line,'        "color14": "',colors[14] + '",\n')
        line = clrc(line,'        "color15": "',colors[15] + '"\n')

        newlines.append(line)

    f = open(globalvars.themepath + '.json', "w", encoding='utf-8')
    f.writelines(newlines)
    f.close()

def wal():
    subprocess.check_output([globalvars.walpath, '-nei', globalvars.staticwallpaperpath, '--backend', backend, '-p', globalvars.themepath])
    # n: Skip setting the wallpaper.
    # e: Skip reloading gtk/xrdb/i3/sway/polybar
    # i: Image path

    if backend == 'xiwal':
        xiwaltopywal()
        subprocess.check_output([globalvars.walpath, '-ne', '--theme', globalvars.themepath + '.json'])

def warnai():
    if not os.path.isdir(globalvars.userdir + '/.themes'):
        os.makedirs(globalvars.userdir + '/.themes')
    os.system(globalvars.waranipath + ' -w -g fantome -xf pastel')

def vscode():
    if os.path.isfile(globalvars.vscodepath):
        os.system(globalvars.vscodepath + ' --install-extension dlasagno.wal-theme')

def bash():
    if os.path.isfile(globalvars.userdir + "/.bashrc"):
        f = open(globalvars.userdir + "/.bashrc", "r")
        data = f.read()
        f.close()

        f = open(globalvars.userdir + "/.bashrc", "r")
        lines = f.readlines()
        f.close()
        
        if "wal " not in data:
            print(fg.red + "WARN: You do not have wal in your .bashrc")
            print("this will make any new terminals automatically get themed")
            print("would you like to put a short wal command in your .bashrc?")
            if input(fg.green + "(Y/n): " + fg.reset).lower() != "n":
                lines.reverse()
                lines.append("wal -net --theme " + globalvars.themepath + ".json > /dev/null\n")
                lines.reverse()

                f = open(globalvars.userdir + "/.bashrc", "w")
                f.writelines(lines)
                f.close()

        


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(fg.red + "You must enter a wallpaper and a backend!")
        exit()
    elif len(sys.argv) <= 2:
        wallpaper = sys.argv[1]
        backend = 'xiwal'
    elif len(sys.argv) <= 3:
        wallpaper = sys.argv[1]
        backend = sys.argv[2]

    ##### setup wallpaper into temp folder
    if os.path.isfile(globalvars.staticwallpaperpath):
        os.remove(globalvars.staticwallpaperpath)
    if os.path.isfile(globalvars.gifwallpaperpath):
        os.remove(globalvars.gifwallpaperpath)
    if wallpaper.endswith(".gif"):
        subprocess.check_output([globalvars.ffmpegpath, '-i', wallpaper, '-vframes', '1', globalvars.staticwallpaperpath])
        subprocess.check_output(['cp', wallpaper, globalvars.gifwallpaperpath])
    else:
        subprocess.check_output(['cp', wallpaper, globalvars.staticwallpaperpath])

    wal()
    bash()
    vscode()
    warnai()