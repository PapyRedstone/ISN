# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:12:04 2016

@author: alexandre.febvre
"""

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
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

data = s.recv(1000).decode()
Map = json.loads(data)
MaptoPrint = [ m[::] for m in Map]

while len(data) != 0:
    data = s.recv(1000).decode()
    if data == "WAITING FOR DATA":
        data = input("Entrez une action --->")
        s.send(data.encode())
    else:
        try:
            if isinstance(json.loads(data),int):
                raise ValueError
            d = [deserialiseur(d) for d in json.loads(data)]
            for ent in d:
                MaptoPrint[ent.pos["x"]][ent.pos["y"]] = ent.name[:1].upper()
            for m in MaptoPrint:
                for x in m:
                    print(x,end="  ")
                print()
            MaptoPrint = [ m[::] for m in Map]
        except ValueError:
            print (data)

s.close()