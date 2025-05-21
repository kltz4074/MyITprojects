import time
import sys
import minescript
#x, y, z = minescript.player().position
#print("player coordinates: " + str(int(x)) + " " + str(int(y)) + " " + str(int(z)))
#print("player name: " + minescript.player().name)
for p in minescript.players():
    x, y, z = p.position
   # print(f"{p.name}: X={int(x)}, Y={int(y)}, Z={int(z)}" + " player Health: " + str(int(p.health)))
    print("player name: " + p.name)
    print("player coordinates: " + str(int(x)) + " " + str(int(y)) + " " + str(int(z)))