#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:56:00 2020

@author: elisabettadinitto
"""
from geometricFigures.shape import Shape

class VLine(Shape):
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l
        
    def paint(self, canv): 
        canv.setpixelOn(self.x, self.y)
        for n in range(self.y, self.y+self.l) :
            canv.setpixelOn(self.x, n)