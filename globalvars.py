import os

### dirs

userdir = os.path.expanduser('~')
projectdir = os.path.abspath(os.path.dirname(__file__))
tempdir = projectdir + "/temp"

########

## files

themepath = tempdir + "/theme"
staticwallpaperpath = tempdir + "/staticwallpaper.png"
gifwallpaperpath = tempdir + "/gifwallpaper.gif"

########

## links

githublink = "https://github.com/kyleraykbs/KyWal"
warnailink = "https://github.com/reorr/warnai"

########

##### program paths

thirdparty = "thirdparty"
thirdpartyfull = projectdir + "/" + thirdparty
warani = thirdpartyfull + "/warnai"

waranipath = warani + "/warnai"
vscodepath = '/bin/code'
walpath = '/bin/wal'
gitpath = '/bin/git'
pippath = '/bin/pip3'
ffmpegpath = '/bin/ffmpeg'
xiwalpath = userdir + '/.local/bin/xiwal'

###################