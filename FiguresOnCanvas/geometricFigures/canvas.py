#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:54:17 2020

@author: elisabettadinitto
"""

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[' '] * width for i in range(height)]

    def setpixelOn(self, row, col):
        self.pixels[row][col] = '*'

    def setpixelOff(self, row, col):
        self.pixels[row][col] = ' '

    def getpixel(self, row, col):
        return self.pixels[row][col]

    def display(self):
        print("\n".join(["".join(row) for row in self.pixels]))