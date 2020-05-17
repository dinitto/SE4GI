#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:00:08 2020

@author: elisabettadinitto
"""

from geometricFigures.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)