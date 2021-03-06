# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:19:56 2016

@author: alexandre.febvre
"""

from gameMotor.game import Game
import socket

Socket = socket.socket()
Socket.bind(("0.0.0.0" ,1001))
print("Waiting for connections")
Socket.listen(5)
client, address = Socket.accept()
print ("{} connected".format(address))

#on creer une map avec des obstacles
Map = []
mapSize = 10
for i in range(mapSize):
    Map.append([1 for x in range(mapSize)])

for x in range(3):
    Map[4][x] = 0
for x in range(7):
    Map[x][5] = 0
Map[6][4] = 0
for x in range(8):
    Map[x+1][8] = 0
for x in range(6):
    Map[8][x+2] = 0

g = Game(Map,client)

Continue = True
while Continue:
    Continue = g.play()
    mapPrint = list()
    for m in Map:
        mapPrint.append([x for x in m])

    for ent in g.entity:
        mapPrint[ent.pos["y"]][ent.pos["x"]] = ent.name[0]

    for m in mapPrint:
        for M in m:
            print(str(M), end="  ")
        print()
        
        
print ("Close")
client.close()
Socket.close()
