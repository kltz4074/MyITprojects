import os
from pystyle import Write, Colors
import Sbanner
import webbrowser
import random

rdn = random.randint(5000000, 10000000000000000)
current_directory = os.path.dirname(os.path.abspath(__file__))

folder_name = 'images'
file_name = 'none.txt'
folder_path = os.path.join(current_directory, folder_name)
os.makedirs(folder_path, exist_ok=True)
with open(os.path.join(folder_path, file_name), 'w', encoding='utf-8') as file:
    file.write(str(rdn))

def btdprint(text, interval = 0.025):
    Write.Print(text, Colors.yellow_to_green, interval)

#print(Colorate.Horizontal(Colors.yellow_to_red, banner.Banner, 1))
btdprint(Sbanner.Banner, 0.00025)
btdprint(Sbanner.textq, 0.025)
inputi = Write.Input(Sbanner.textu, Colors.yellow_to_green, interval=0.025)

if int(inputi) == rdn:
    Write.Input(Sbanner.scrbn, Colors.red, interval=0.00025)
    btdprint(Sbanner.scrbn, 0.00025)

if inputi == "1":
    os.startfile(os.path.abspath("files/videos/video1.mp4"))
    
        
if inputi == "2":
    Write.Print(Sbanner.telegram, Colors.yellow_to_green, interval=0.025)
    inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

    if inputg == "1":
        
        btdprint(Sbanner.tgks, 0.025)
        inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
        
        if inputgk == "1":
            webbrowser.open('https://t.me/kltzyoutube_pon')

if inputi == "3":
    smalgnrt = int(Write.Input("от - ", Colors.yellow_to_green, interval=0.025))
    biggnrt = int(Write.Input("до - ", Colors.yellow_to_green, interval=0.025))
    btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)  # Преобразование числа в строку