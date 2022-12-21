import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

f = open(os.path.expanduser("~") + "/.cache/wal/colors")
colorsraw = f.readlines()
colors = []
for clr in colorsraw:
    colors.append(clr.strip())

f = open("template.rasi", "r")
data = f.read()
f.close()

data = data.replace("CLR1", colors[0])
data = data.replace("CLR2", colors[5])
data = data.replace("CLR3", colors[2])
data = data.replace("CLR4", colors[1])
data = data.replace("CLR5", colors[4])
data = data.replace("CLR6", colors[5])

f = open("pywal.rasi", "w")
f.write(data)
f.close()

print("Rofi color file generated at: '" + os.getcwd() + "/pywal.rasi' please use this in any rofi scripts that you want to use your color pallette")