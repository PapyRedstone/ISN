# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:35:55 2016

@author: alexandre.febvre
"""

import socket
import json
from gameMotor.entity import EntForDeserializeur

def deserialiseur(obj_dict):
    if "__class__" in obj_dict:
        if obj_dict["__class__"] == "Entity":
            obj = EntForDeserializeur(obj_dict["name"],obj_dict["pos"])
            return obj

s = socket.socket()         # Create a socket object
host = socket.gethostbyname(socket.gethostname())    # Get serveur machine name
port = 1001
s.connect((host, port))
s.settimeout(1)

data = s.recv(10000).decode()
Map = json.loads(data)
data = ""
entPos = list()

def setEntPos(data):
    entity = [deserialiseur(d) for d in json.loads(data)]
    for ent in entity:
        entPos.append({"name":ent.name,"x":ent.pos["x"],"y":ent.pos["y"]})
    
def send(txt):
    data = s.recv(1000).decode()
    print(data)
    if data == "WAITING FOR DATA":
        s.send(txt.encode())
        data = s.recv(1000).decode()
        setEntPos(data)
    else:
        setEntPos(data)
        print(entPos)
        