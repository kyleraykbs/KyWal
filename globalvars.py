import os

### dirs

userdir = os.path.expanduser('~')
projectdir = os.path.abspath(os.path.dirname(__file__))
tempdir = projectdir + "/temp"
modulesdir = projectdir + "/modules"

########

#### APPS

appsdir = modulesdir + "/APPS"

rofidir = appsdir + "/rofi"
rofiapp = rofidir + "/rofi.py"

#########

#### external modules

extmodulesdir = modulesdir + "/external"

swwwextmoddir = extmodulesdir + "/swww.py"
oomoxextmoddir = extmodulesdir + "/oomox.py"

#####################

## files

themepath = tempdir + "/theme"
staticwallpaperpath = tempdir + "/staticwallpaper.png"
gifwallpaperpath = tempdir + "/gifwallpaper.gif"
firsttimesetup = tempdir + "/FirstTimeSetup"
autothemedewm = tempdir + "/ThemeDEWM"

########

## links

githublink = "https://github.com/kyleraykbs/KyWal"
warnailink = "https://github.com/reorr/warnai"

########

# modules

Hyprlanddir = modulesdir + "/WM/Hyprland.py"

#########

##### program paths

thirdparty = "thirdparty"
thirdpartyfull = projectdir + "/" + thirdparty
warani = thirdpartyfull + "/warnai"

waranipath = warani + "/warnai"
vscodepath = '/bin/code'
bashpath = '/bin/bash'
walpath = '/bin/wal'
gitpath = '/bin/git'
pippath = '/bin/pip3'
ffmpegpath = '/bin/ffmpeg'
xiwalpath = userdir + '/.local/bin/xiwal'
steamrootpath = userdir + '/.steam/root'
walsteampath = userdir + "/.local/bin/wal-steam"

###################