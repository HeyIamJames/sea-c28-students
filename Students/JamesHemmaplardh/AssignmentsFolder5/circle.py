#!/usr/bin/env python
"""circle class --
fill this in so it will pass all the tests.
"""
import math

class Circle(object):

    def __init__(self, radius):
         self.radius = radius

    def _diamater_(self):
        return self.radius * 2

    def _diamater2_(self, diameter):
        self.radius = diameter / 2

    diameter = property(_diamater_, _diamater2_)
