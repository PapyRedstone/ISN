# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:23:37 2016

@author: alexandre.febvre
"""

from gameMotor.entity import Entity

class Object(Entity):
    """
    Class de base definissant un objet
    """
    def __init__(self, pos, Map):
        Entity.__init__(self, pos, Map)