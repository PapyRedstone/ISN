# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:53:02 2016

@author: alexandre.febvre
"""

class Entity:
    """
    Classe de base définissant les objets du jeu
    """
    def __init__(self, pos, Map , power = 0):
        self.pos = pos
        self.map = Map
        self.name = "Entity"
        self.power = power
        self.pv = 1
    
    def mouv(self, data):   #data contient le deplacement de l'entite
        #pour chaque direction possible en test si data est egale
        #si oui on bouge l'entite suivant cette axe
        if data == "UP":
            tmpPos = self.pos["y"]-1
            if tmpPos < 0:
                tmpPos = tmpPos +1
            elif self.map[tmpPos][self.pos["x"]] == 0:
                tmpPos = self.pos["y"]     
            self.pos["y"] = tmpPos
        
        elif data == "DOWN":
            tmpPos = self.pos["y"]+1
            if tmpPos >= len(self.map):
                tmpPos = tmpPos -1
            elif self.map[tmpPos][self.pos["x"]] == 0:
                tmpPos = self.pos["y"]
            self.pos["y"] = tmpPos

        elif data == "RIGHT": 
            tmpPos = self.pos["x"]+1
            if tmpPos >= len(self.map[0]):
                tmpPos = tmpPos -1
            elif self.map[self.pos["y"]][tmpPos] == 0:
                tmpPos = self.pos["x"]
            self.pos["x"] = tmpPos
        
        elif data == "LEFT": 
            tmpPos = self.pos["x"]-1
            if tmpPos < 0:
                tmpPos = tmpPos +1
            elif self.map[self.pos["y"]][tmpPos] == 0:
                tmpPos = self.pos["x"]
            self.pos["x"] = tmpPos
        
    def attack(self, target):
        #on fait perdre a target autant de pv que la valeur de dommage
        target.pv = target.pv - self.power
        
class EntForDeserializeur(Entity):
    def __init__(self,name,pos):
        Entity.__init__(self,pos,[])
        self.name = name