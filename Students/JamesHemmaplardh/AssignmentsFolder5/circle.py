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

    def _diamateradius2_(self, diameter):
        self.radius = diameter / 2

    diameter = property(_diamater_, _diamateradius2_)
 

    def _get_area(self):
        return math.pi * (self.radius ** 2)

    area = property(_get_area)

    def __str__(self):
        string = u'Circle with radius: ' + format(self.radius, '.6f')
        return string


    def __repr__(self):
        string = u'Circle({0!r})'.format(self.radius)
        return string


    def __add__(self, other):
        radius1 = self.radius
        radius2 = other.radius
        circ = Circle(radius1 + radius2)
        return circ




