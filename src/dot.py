from __future__ import annotations
from math import sqrt
from random import *

class Dot:

    def __init__(self, dimention):
        #Inisialisasi dot
        self.coordinates = []

        for i in range(dimention):
            self.coordinates.append(round(uniform(-100000, 100000), 3))

        
    def displayDot(self):
        # Meng-output dot dalam format (x, y, z)
        #print("({x1}, {y1}, {z1})".format(x1 = self.x, y1 = self.y, z1 = self.z))
        print("(", end="")
        for i in range (len(self.coordinates)-1):
            print("{x},".format(x = self.coordinates[i]),  end="")

        print("{y}".format(y=self.coordinates[i+1]), end="")
        print(")")

    def distanceTwoDots(self, otherDot: Dot):
        # Menghitung jarak antara dua buah dot

        # squareX = (self.x - otherDot.x)**2
        # squareY = (self.y - otherDot.y)**2
        # squareZ = (self.z - otherDot.z)**2
        # return sqrt(squareX + squareY + squareZ)

        sumAll = 0

        for i in range(len(self.coordinates)):
            sumAll += (self.coordinates[i] - otherDot.coordinates[i])**2

        return sqrt(sumAll)

    def isEqual(self, otherDot: Dot):
        # Menentukan apakah dua dot berlokasi di koordinat yang sama atau tidak
        # (x1, y1, z1) = (x2, y2, z2)
        equal = True

        for i in range(len(self.coordinates)):
            if(self.coordinates[i] != otherDot.coordinates[i]):
                equal = False
        
        return equal
    

class PairOfDots:
    def __init__(self, p1, p2, distance):
        # Inisialisasi PairOfDots
        self.p1 = p1
        self.p2 = p2
        self.distance = distance


    