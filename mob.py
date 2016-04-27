# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:53:04 2016

@author: alexandre.febvre
"""

from gameMotor.entity import Entity
from gameMotor.aStar import pathfinding
from random import randint

class Mob(Entity):
    """
    Classe définissant un monstre et ses actions
    """
    def __init__(self, Map, pos = {"x":0,"y":0}, pv = 10, power = 1):
        Entity.__init__(self,pos,Map,power)
        self.name = "Mob"
        self.pv = pv 
        self.path = []
        self.state = "FindP"       
    
    def play(self, entity):
        print("mob play")
        for ent in entity:
            if ent.name == "Player":
                perso = ent        
        pMob = self.pos
        try:
            pPos = perso.pos
        except UnboundLocalError:
            return
        nearFromP = 2
        farFromP = 10
        
        MapWithEntity = []
        for m in self.map:
            MapWithEntity.append([x for x in m])
            
        for ent in entity:
            if ent.name == "Player" or ent.name == "Mob":
                MapWithEntity[ent.pos["y"]][ent.pos["x"]] = 0

        if self.state == "FindP":
            try:
                if len(self.path) <= 0:
                    self.findPath(perso.pos,self.map)
            except TypeError:
                pass
            self.moveOnPath()
            if (pMob["x"]-pPos["x"]<nearFromP and pMob["x"]-pPos["x"]>-nearFromP and
                pMob["y"]-pPos["y"]<nearFromP and pMob["y"]-pPos["y"]>-nearFromP):
                self.state = "AttackP"
                self.path = list()
                
        elif self.state == "AttackP":
            self.attack(perso)
            if self.pv <= 5:
                self.state = "FleeP"
                self.path = list()
            if not (pMob["x"]-pPos["x"]<nearFromP and pMob["x"]-pPos["x"]>-nearFromP and
                pMob["y"]-pPos["y"]<nearFromP and pMob["y"]-pPos["y"]>-nearFromP):
                self.state = "FindP"
                
            elif pPos == None:
                self.state = "FindP"
                self.path = list()
                
        elif self.state == "FleeP":
            try:
                if len(self.path) <= 0:
                    posAlea = {"x":randint(0,len(self.map[0])),"y":randint(0,len(self.map))}
                    self.findPath(posAlea,MapWithEntity)
            except TypeError:
                pass
            self.moveOnPath()
            if (self.pos["x"]-pPos["x"]>farFromP and self.pos["x"]-pPos["x"]<-farFromP and
                self.pos["y"]-pPos["y"]>farFromP and self.pos["y"]-pPos["y"]<-farFromP):
                self.state = "FindP"
                self.path = list()
                
            
    def findPath(self,target,Map):
        self.path = pathfinding(Map,self.pos,target)    #on trouve un chemin
        
        
    def moveOnPath(self):
        try:
            if len(self.path) > 0:      #si un chemin existe
                self.mouv(self.path[0]) #on va a la prochaine case du chemin
                self.path.pop(0)        #on supprime la derniere case du chemin

        except TypeError:
            pass