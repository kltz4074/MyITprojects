import pystyle

def btdprint(text, color = pystyle.Colors.yellow_to_green, speed = 0.025):
    pystyle.Write.Print(text, color, speed)
    print(" ")
    
def btdinput():
    pystyle.Write.Input(">>", pystyle.Colors.yellow_to_green, 0.025)
    print(" ")
    
btdprint("напиши")

inpt = btdinput()

print(inpt)