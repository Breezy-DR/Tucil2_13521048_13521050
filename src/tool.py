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

def calculateClosest(pointList ):  # bidang pembatas ditengah (x, 0, 0)

    # BASIS 
    if(len(pointList) == 2):

        closestPair = PairOfDots(pointList[0], 
                                pointList[1], 
                                pointList[0].distanceTwoDots(pointList[1]))
        
        return closestPair

    elif (len(pointList) == 3):
        
        closestPair = PairOfDots(pointList[0], 
                                pointList[1], 
                                pointList[0].distanceTwoDots(pointList[1]))

        if(pointList[0].distanceTwoDots(pointList[2]) < closestPair.distance):
            closestPair.p2 = pointList[2]
            closestPair.distance = pointList[0].distanceTwoDots(pointList[2])
        
        elif (pointList[1].distanceTwoDots(pointList[2]) < closestPair.distance):
            closestPair.p1 = pointList[1]
            closestPair.p2 = pointList[2]
            closestPair.distance = pointList[1].distanceTwoDots(pointList[2])

        return closestPair
    
    

points = randomSorted(3)

for i in range(3):
    points[i].displayDot()

closestPair = calculateClosest(points)

print("\nClosest Pair: ")
closestPair.p1.displayDot()
closestPair.p2.displayDot()
print(closestPair.distance)
