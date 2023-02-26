from __future__ import annotations
from math import sqrt

class Dot:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def displayDot(self):
        print("({x1}, {y1}, {z1})".format(x1 = self.x, y1 = self.y, z1 = self.z))

    def distanceTwoDots(self, otherDot: Dot):
        squareX = (self.x - otherDot.x)**2
        squareY = (self.y - otherDot.y)**2
        squareZ = (self.z - otherDot.z)**2
        return sqrt(squareX + squareY + squareZ)

    def isEqual(self, otherDot: Dot):
        if (self.x == otherDot.x and self.y == otherDot.y and self.z == otherDot.z):
            return True
        return False 

    def getX(self):
        return self.x
    

class PairOfDots:
    def __init__(self, p1, p2, distance):
        self.p1 = p1
        self.p2 = p2
        self.distance = distance


    