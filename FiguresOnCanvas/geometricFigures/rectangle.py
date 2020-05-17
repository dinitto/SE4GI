#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:58:05 2020

@author: elisabettadinitto
"""
from geometricFigures.shape import Shape
from geometricFigures.hline import HLine
from geometricFigures.vline import VLine

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
 
    def paint(self, canv):
        hl1 = HLine(self.x, self.y, self.w)
        hl1.paint(canv)
        hl2 = HLine(self.x, self.y + self.h, self.w)
        hl2.paint(canv)
        vl1 = VLine(self.x, self.y, self.h)
        vl1.paint(canv)
        vl2 = VLine(self.x + self.w, self.y, self.h)
        vl2.paint(canv)