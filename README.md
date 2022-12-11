# KyWal : ``>UNIVERSAL<  system themer using Python and PyWal``

# NOT FINISHED YET

### Missing Features (will be added within the next week)
- wallpaper
- window manager theme
- rofi theme
- discord theme
- pywalfox autoinstall
- gif wallpapers
- razer keyboard theme
- steam theme (possibly)

## Description

To sum it up, this is a mess of utilites stringed together in combination with some scripts I whipped up in python.

Basically you can theme your whole systems color pallette/themes to match your wallpaper with one command and a few seconds of wait time

### Used Repositories:
https://github.com/reorr/warnai

# Installation

### Dependencies
Arch Linux
- pywal-16-colors
- git
- python-pip
- python
- ffmpeg
- optipng
- inkscape
- qt5-styleplugins (optional) *for making QT apps use the GTK theme*

**install dependencies**

``
yay -S pywal-16-colors git python-pip python ffmpeg optipng inkscape qt5-styleplugins
``

**clone repo to wherever**

``
git clone https://github.com/kyleraykbs/KyWal
``

### Optional

- set gtk2 as your qt style in your qt theme setter (qt5ct, etc)
- install the "Wal Theme" for vscode or run the script then enable it
*(https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme)*

# Running

``
python path/to/repo/main.py
``

### Post First Run Setup

- open your gtk theme changer *(lxappearance, etc)* of choice and set your primary theme to warnai