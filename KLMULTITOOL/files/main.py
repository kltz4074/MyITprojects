import os
from pystyle import Write, Colors
import SbannerRU
import SbannerENG
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

btdprint("Выберите язык / Choose language 1 - RU, 2 - ENG", 0.025)
print(" ")
print(" ")
lng = Write.Input(">>", Colors.yellow_to_green, interval=0.025)

if lng == "2":
    btdprint(SbannerENG.Banner, 0.00025)
    btdprint(SbannerENG.textq, 0.025)
    inputi = Write.Input(SbannerENG.textu, Colors.yellow_to_green, interval=0.025)

    if int(inputi) == rdn:
        Write.Input(SbannerENG.scrbn, Colors.red, interval=0.00025)
        btdprint(SbannerENG.scrbn, 0.00025)
        
    if inputi == "1":
        Write.Print(SbannerENG.telegram, Colors.yellow_to_green, interval=0.025)
        inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

        if inputg == "1":
            btdprint(SbannerENG.tgks, 0.025)
            inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

            if inputgk == "1":
                webbrowser.open('https://t.me/kltzyoutube_pon')

    if inputi == "2":
        smalgnrt = int(Write.Input("from - ", Colors.yellow_to_green, interval=0.025))
        biggnrt = int(Write.Input("to - ", Colors.yellow_to_green, interval=0.025))
        btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)
        print(" ")


if lng == "1":
    btdprint(SbannerRU.Banner, 0.00025)
    btdprint(SbannerRU.textq, 0.025)
    inputi = Write.Input(SbannerRU.textu, Colors.yellow_to_green, interval=0.025)

    if int(inputi) == rdn:
        Write.Input(SbannerRU.scrbn, Colors.red, interval=0.00025)
        btdprint(SbannerRU.scrbn, 0.00025)
        
    if inputi == "1":
        Write.Print(SbannerRU.telegram, Colors.yellow_to_green, interval=0.025)
        inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

        if inputg == "1":
            btdprint(SbannerRU.tgks, 0.025)
            inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

            if inputgk == "1":
                webbrowser.open('https://t.me/kltzyoutube_pon')

    if inputi == "2":
        smalgnrt = int(Write.Input("от - ", Colors.yellow_to_green, interval=0.025))
        biggnrt = int(Write.Input("до - ", Colors.yellow_to_green, interval=0.025))
        btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)
        print(" ")