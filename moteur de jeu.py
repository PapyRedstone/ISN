# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:19:56 2016

@author: alexandre.febvre
"""

from gameMotor.game import Game
import socket
import json

Socket = socket.socket()
Socket.bind((socket.gethostbyname(socket.gethostname()) ,15555))
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
        if ent.name == "Mob":
            mapPrint[ent.pos["y"]][ent.pos["x"]] = "M"
        elif ent.name == "HealthObject":
            mapPrint[ent.pos["y"]][ent.pos["x"]] = "H"
        elif ent.name == "Player":
            mapPrint[ent.pos["y"]][ent.pos["x"]] = "J"
        elif ent.name == "PowerObject":
            mapPrint[ent.pos["y"]][ent.pos["x"]] = "P"

    for m in mapPrint:
        for M in m:
            print(str(M), end="  ")
        print()
        
    sendTab = json.dumps(g.map+g.entity)
    client.send(sendTab.encode())
    response = client.recv(1000).decode()
    if response != "ACCOMPLISH":
        print ("DATA RECEIVED BY USER ARE UNCOMPLET")
        
print ("Close")
client.close()
Socket.close()
