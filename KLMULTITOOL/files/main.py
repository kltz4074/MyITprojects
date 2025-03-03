import os
from pystyle import Write, Colors
import Sbanner
import webbrowser
def btdprint(text, interval = 0.025):
    Write.Print(text, Colors.yellow_to_green, interval)
    
def btdinput(text = ">>"):
    Write.Input(text, Colors.yellow_to_green, interval=0.025)

#print(Colorate.Horizontal(Colors.yellow_to_red, banner.Banner, 1))
btdprint(Sbanner.Banner, 0.00025)
btdprint(Sbanner.textq, 0.025)
input = Write.Input(Sbanner.textu, Colors.yellow_to_green, interval=0.025)


if input == "1":
    os.startfile(os.path.abspath("files/videos/video1.mp4"))
    
if input == "2":
    btdprint(Sbanner.whatDownload)
    inputlk = btdinput()
    if inputlk == "1":
        print("download modrinth, ok!")
        os.startfile('files\Modrinth_App_0.9.3_x64-setup.exe')
    
    if inputlk == "2":
        print("mmm, multiMC? good choice!")
        webbrowser.open('https://files.multimc.org/downloads/mmc-develop-win32.zip')
    if inputlk == "3":
        webbrowser.open('https://github.com/PrismLauncher/PrismLauncher/releases/download/9.2/PrismLauncher-Windows-MSVC-Setup-9.2.exe')
        
if input == "3":
    Write.Print(Sbanner.telegram, Colors.yellow_to_green, interval=0.025)
    inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
    
    if inputg == "1":
        
        btdprint(Sbanner.tgks, 0.025)
        inputgk = btdinput()
        
        if inputgk == "1":
            webbrowser.open_new("https://t.me/kltzyoutube_pon")