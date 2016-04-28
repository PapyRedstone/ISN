# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:59:49 2016

@author: alexandre.febvre
"""

from gameMotor.mob import Mob
from gameMotor.perso import Perso
from gameMotor.healthobject import HealthObject
from gameMotor.powerobject import PowerObject
from random import randint

class Game:
    """
    Fonction contenant la map, les joueurs et les monstres
    """
    def __init__(self,Map,client,nbMonster = 5):
        self.map = Map      #contient la map du donjon : 
                            #1 est franchissable 
                            #0 est infranchissable
        self.client = client
        self.entity = []
        self.entity.append(Perso(Map,pos = {"x":len(Map[0])-1,"y":len(Map)-1}))
        for i in range(nbMonster):
            randPos = {"x":randint(0,len(Map)-1),"y":randint(0,len(Map)-1)}
            while self.map[randPos["y"]][randPos["x"]] == 0:
                randPos = {"x":randint(0,len(Map)-1),"y":randint(0,len(Map)-1)}
            self.entity.append(Mob(Map,randPos))
        self.entity.append(HealthObject({"x":0,"y":0}, Map))
        self.entity.append(PowerObject({"x":1,"y":0}, Map))
    
    def play(self):
        answer = True
        for ent in self.entity:
            if ent.name == "Player":
                answer = ent.play(self.entity,self.client)
                if ent.pv <= 0:
                    answer = False
            else:
                ent.play(self.entity)
            if ent.pv <= 0:
                self.entity.remove(ent)
        
        return answer