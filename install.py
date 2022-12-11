import subprocess
import os
import importlib
import globalvars

from customcolors import *

os.chdir(os.path.abspath(os.path.dirname(__file__)))

def checkDependancy(deppath, name = None):
    if name == None:
        name = deppath

    if not os.path.exists(deppath):
        print(fg.red + "ERROR: Missing dependancy " + name)
        return False
    else:
        print(fg.green + name + " dependancy check passed! already installed!")
        return True

def checkThirdParty():
    if os.path.exists(globalvars.thirdparty):
        return True
    else:
        os.mkdir(globalvars.thirdparty)
        return False

def checkWarnai():
    def installWarnai():
        print(fg.cyan + "Warani not installed cloning..." + fg.reset)
        output = subprocess.check_output(['git', 'clone', globalvars.warnailink, globalvars.warani])
        print(fg.green + "Warani install finished (hopefully)")

    if checkThirdParty():
        if not os.path.isdir(globalvars.warani):
            installWarnai()
        else:
            print(fg.green + "warnai dependancy check passed! already installed!")
    else:
        installWarnai()

def checkPipPackage(package):
    if package not in subprocess.check_output([globalvars.pippath, 'list']).decode('utf-8'):
        print(fg.cyan + package + " not installed. Installing..." + fg.reset)
        subprocess.check_output([globalvars.pippath, 'install', package])
        print(fg.green + package + " install finished (hopefully)")
    else:
        print(fg.green + package + " backend already installed!")



##### Main check
def checkForDependancies():
    DependancyCheckPassed = True

    if not checkDependancy(globalvars.gitpath, "git"): DependancyCheckPassed = False
    if not checkDependancy(globalvars.walpath, "pywal-16-colors"): DependancyCheckPassed = False
    if not checkDependancy(globalvars.pippath, "python-pip"): DependancyCheckPassed = False
    if not checkDependancy(globalvars.ffmpegpath, "ffmpeg"): DependancyCheckPassed = False
    
    if not checkDependancy('/bin/optipng', "optipng"): DependancyCheckPassed = False
    if not checkDependancy('/bin/inkscape', "inkscape"): DependancyCheckPassed = False
    checkWarnai()

    print(fg.yellow + "backends======")
    checkPipPackage('colorz')
    checkPipPackage('haishoku')
    checkPipPackage('xiwal')
    print(fg.yellow + "==============")

    # make dirs
    if not os.path.isdir(globalvars.tempdir):
        os.makedirs(globalvars.tempdir)

    if DependancyCheckPassed:
        return True
    else:
        return False

if __name__  == "__main__":
    checkForDependancies()