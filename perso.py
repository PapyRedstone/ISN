# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:55:15 2016

@author: alexandre.febvre
"""

from gameMotor.entity import Entity
from random import choice

class Perso(Entity):
    """
    Classe définissant un joueur et ses actions
    """
    def __init__(self, Map, pos = {"x":0,"y":0}):
        Entity.__init__(self, pos, Map, 5)
        self.name = "Player"
        self.pv = 100
    
    def play(self, entity, client):
        client.send("WAITING FOR DATA".encode())
        data = client.recv(1000).decode()
        print("PV:",self.pv)
#==============================================================================
#         data = input("Action joueur -->") #donée rentrée par l'utilisateur 
#                                             #temporaire
#==============================================================================
        if not data:    #si data vaut None alors on retourne une erreur
            print("Erreur : pas de donnes utilisateur")
            return True
        else:           #sinon on fait l'action demande
            self.mouv(data)
            if data == "ATTACK":
                mobsNear = []
                for ent in entity:
                    if (ent.pos["x"]-self.pos["x"] > -2 and
                        ent.pos["x"]-self.pos["x"] < 2 and
                        ent.pos["y"]-self.pos["y"] > -2 and
                        ent.pos["y"]-self.pos["y"] < 2 and
                        ent.name == "Mob"):
                        mobsNear.append(ent)
                try:
                    self.attack(choice(mobsNear))
                except IndexError:
                    pass
            elif data.lower() == "q":
                return False
            else:
                print("Pas d'action repertorié")
            
            return True