# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:22:19 2016

@author: alexandre.febvre
"""

from gameMotor.object import Object

class PowerObject(Object):
    
    def __init__(self, pos, Map, additionnalPower = 5):
        Object.__init__(self, pos, Map)
        self.name = "PowerObject"
        self.additionnalPower = additionnalPower
    
    def play(self,entity):        
        for ent in entity:
            if ent != self:
                if ent.pos == self.pos:
                    ent.power = ent.power + self. additionnalPower
                    self.pv = 0