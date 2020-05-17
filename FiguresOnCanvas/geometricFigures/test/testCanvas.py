#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:52:49 2020

@author: elisabettadinitto
"""

import unittest
from geometricFigures.canvas import Canvas

class TestCanvas(unittest.TestCase):
    def testPixelOn(self):
        c = Canvas(10, 10)
        c.setpixelOn(4, 4)
        self.assertEqual(c.getpixel(4, 4), '*')
        
    def testPixelOff(self):
        c = Canvas(10, 10)
        c.setpixelOff(4, 4)
        self.assertEqual(c.getpixel(4, 4), ' ')
        
        
if __name__ == '__main__':
   unittest.main()
        
 