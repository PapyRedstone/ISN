# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:12:04 2016

@author: alexandre.febvre
"""

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import json

#==============================================================================
# s = socket.socket()         # Create a socket object
# host = socket.gethostbyname(socket.gethostname())    # Get serveur machine name
# port = 134              # Reserve a port for your service.
#==============================================================================

#s.close()                     # Close the socket when done


s = socket.socket()         # Create a socket object
host = socket.gethostbyname(socket.gethostname())    # Get serveur machine name
port = 15555
s.connect((host, port))
while True:
    data = s.recv(1000).decode()
    if data == "WAITING FOR DATA":
        data = input("Entrez une action --->")
        s.send(data.encode())
    else:
        Map = json.load(data[0])
        s.send("ACCOMPLISH".encode())
        print (Map)
        print(data[1])
