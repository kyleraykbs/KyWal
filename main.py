import os
origdir = os.getcwd()
import install
import globalvars
import sys
import subprocess
from customcolors import *

os.chdir(os.path.abspath(os.path.dirname(__file__)))

if not install.checkForDependancies():
    print(fg.red + "ERROR: Some dependancies could not be found please install them with the instructions on the github!")
    print(fg.reset + globalvars.githublink)
    exit()

def YNPrompt():
    return (input(fg.lightgreen + "(Y/n): " + fg.reset) != "n")

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

def pywalfox():
    if os.path.exists(globalvars.userdir + "/.local/bin/pywalfox"):
        os.system(globalvars.userdir + "/.local/bin/pywalfox update")

def rofi():
    os.system("python '" + globalvars.rofiapp + "'")

def oomox():
    os.system("python '" + globalvars.oomoxextmoddir + "'")

def vscode():
    if os.path.isfile(globalvars.vscodepath):
        os.system(globalvars.vscodepath + ' --install-extension dlasagno.wal-theme')

def bash(noprompt = False):
    if os.path.isfile(globalvars.userdir + "/.bashrc"):
        f = open(globalvars.userdir + "/.bashrc", "r")
        data = f.read()
        f.close()

        f = open(globalvars.userdir + "/.bashrc", "r")
        lines = f.readlines()
        f.close()
        
        if "wal " not in data:
            if not noprompt:
                print(fg.red + "WARN: You do not have wal in your .bashrc")
                print("this will make any new terminals automatically get themed")
                print("would you like to put a short wal command in your .bashrc?")
            if noprompt or (input(fg.green + "(Y/n): " + fg.reset).lower() != "n"):
                lines.reverse()
                lines.append("wal -net --theme " + globalvars.themepath + ".json > /dev/null &\n")
                lines.reverse()

                f = open(globalvars.userdir + "/.bashrc", "w")
                f.writelines(lines)
                f.close()
            print("added: 'wal -net --theme " + globalvars.themepath + ".json > /dev/null &\n' to the top of .bashrc")

################
supportedenvs = {
    "Hyprland":globalvars.Hyprlanddir
}
################

def themeuserenv(): ### Detect the current WM / DE and see if we support it
    curenv = subprocess.getoutput('echo $XDG_CURRENT_DESKTOP').strip()
    print(curenv)
    if curenv in supportedenvs:
        if not os.path.isfile(globalvars.autothemedewm):
            print(fg.green + "It appears your DE/WM (" + curenv + ") is supported!")
            print("would you like to change its config automatically from now on?")
            if YNPrompt():
                f = open(globalvars.autothemedewm, "w")
                f.write("y")
                f.close()
            else:
                f = open(globalvars.autothemedewm, "w")
                f.write("n")
                f.close()

        f = open(globalvars.autothemedewm, "r")
        shouldthemedewm = f.read().strip() == "y"
        f.close()

        if shouldthemedewm:
            envscript = supportedenvs[curenv]
            os.system("export PYTHONPATH='" + globalvars.projectdir + "'; python '" + envscript + "'")

def firstTimeSetup():
    if os.path.exists(globalvars.autothemedewm):
        os.remove(globalvars.autothemedewm)
    print("")
    print(bg.cyan + "First Time Setup" + bg.reset)
    print(bg.cyan + "It appears this is the first time you have run KyWal!")
    print(bg.cyan + "Welcome, would you like to automatically setup some themes?")
    print(bg.cyan + "(Dont worry there will be a (Y/n) prompt for each step)" + bg.reset)
    if input(fg.lightgreen + "(Y/n): " + fg.reset) != "n":
        print("")
        print("Would you like to make your terminal automatically get themed after opening?")
        print("aka do you want: wal -net --theme " + globalvars.themepath + ".json > /dev/null &\n")
        print("put at the top of your .bashrc? (it should run instantly)")
        print("((if its already there nothing will be added))")
        if YNPrompt():
            bash(True)
        print("")
        print("Would you like to install the Wal VSCode theme?")
        print("you will have to manually enable it in vscode extensions")
        if YNPrompt():
            vscode()
    print("")

    # Create the first time setup file so we dont run again
    f = open(globalvars.firsttimesetup, "w")
    f.close()

    print(fg.green + "First time setup complete!" + fg.reset)
    input("(press enter to continue)")

def printHelp():
    print("--help : print help")
    print("--first-time-setup : re-run first time setup")

if __name__ == "__main__":
    if "--first-time-setup" in sys.argv:
        sys.argv.remove('--first-time-setup')
        if os.path.exists(globalvars.firsttimesetup):
            os.remove(globalvars.firsttimesetup)
    
    if ("--help" in sys.argv) or ("-h" in sys.argv):
        printHelp()
        exit()

    if len(sys.argv) <= 1:
        print(fg.red + "You must enter a wallpaper and a backend!")
        exit()
    elif len(sys.argv) <= 2:
        wallpaper = origdir + "/" + sys.argv[1]
        backend = 'xiwal'
    elif len(sys.argv) <= 3:
        wallpaper = origdir + "/" + sys.argv[1]
        backend = sys.argv[2]

    print(wallpaper)

    ##### setup wallpaper into temp folder
    if os.path.isfile(globalvars.staticwallpaperpath):
        os.remove(globalvars.staticwallpaperpath)
    if os.path.isfile(globalvars.gifwallpaperpath):
        os.remove(globalvars.gifwallpaperpath)
    if wallpaper.endswith(".gif"):
        subprocess.check_output([globalvars.ffmpegpath, '-i', wallpaper, '-vframes', '1', globalvars.staticwallpaperpath])
        subprocess.check_output(['cp', wallpaper, globalvars.gifwallpaperpath])
    else:
        if wallpaper.endswith(".png"):
            subprocess.check_output(['cp', wallpaper, globalvars.staticwallpaperpath])
        else:
            print("converting file to png please wait")
            subprocess.check_output(['convert', wallpaper, globalvars.staticwallpaperpath])
            print("done converting")

    wal()

    ### IF we are on first time setup
    if not os.path.isfile(globalvars.firsttimesetup):
        firstTimeSetup()
    ###

    themeuserenv()
    rofi()
    pywalfox()
    oomox()
    warnai()