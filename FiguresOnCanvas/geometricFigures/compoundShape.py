#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:01:47 2020

@author: elisabettadinitto
"""
from geometricFigures.shape import Shape

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes
 
    def paint(self, canv):
        for s in self.shapes:
            s.paint(canv)