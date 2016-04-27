# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:42:37 2016

@author: alexandre.febvre
"""

from gameMotor.object import Object

class HealthObject(Object):
    """
    """
    def __init__(self, pos, Map, restoreHealth = 5):
        Object.__init__(self, pos, Map)
        self.name = "HealthObject"
        self.restoreHealth = restoreHealth
    
    def play(self,entity):        
        for ent in entity:
            if ent != self:
                if ent.pos == self.pos:
                    ent.pv = ent.pv + self.restoreHealth
                    self.pv = 0