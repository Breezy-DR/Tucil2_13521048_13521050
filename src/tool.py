from dot import *
from random import *


# Menghasilkan list point yang random tapi terurut
# berdasarkan nilai sumbu x
def randomSorted(n):

    pointList = []

    for i in range (0,n):
        point = Dot(randrange(0, 100), randrange(0, 100), randrange(0, 100))
        print(i)
        pointList.append(point)

    pointList = sorted(pointList, key=lambda Dot: Dot.x)

    return pointList

