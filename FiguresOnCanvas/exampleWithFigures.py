#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:06:10 2020

@author: elisabettadinitto
"""

from geometricFigures.canvas import Canvas
from geometricFigures.rectangle import Rectangle
from geometricFigures.compoundShape import CompoundShape

c = Canvas(20, 20)
r = Rectangle(0, 0, 10, 15)
r1 = Rectangle(0, 1, 5, 7)
r2 = Rectangle(2, 3, 4, 10)
r.paint(c)
cs = CompoundShape([r1, r2])
cs.paint(c)
c.display()