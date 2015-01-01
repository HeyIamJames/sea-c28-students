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
 

    def _getarea_(self):
        return math.pi * (self.radius ** 2)

    area = property(_getarea_)

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

    def __mul__(self, other):
        circ = Circle(self.radius * other)
        return circ


    def __eq__(self, other):
        if self.radius == other.radius:
            return True


    def __le__(self, other):
        if self.radius <= other.radius:
            return True

