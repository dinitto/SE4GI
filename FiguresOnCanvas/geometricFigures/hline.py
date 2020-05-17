#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:52:17 2020

@author: elisabettadinitto
"""
#import shape
#import canvas

from geometricFigures.shape import Shape

class HLine(Shape):
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l
        
    def paint(self, canv): 
        canv.setpixelOn(self.x, self.y)
        for n in range(self.x, self.x+self.l) :
            canv.setpixelOn(n, self.y)