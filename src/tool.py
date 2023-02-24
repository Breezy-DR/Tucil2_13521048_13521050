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

def bruteforceClosest(pointList):

    if(len(pointList) > 1):
        closestPair = PairOfDots(pointList[0], 
                                pointList[1], 
                                pointList[0].distanceTwoDots(pointList[1]))

        for i in pointList:
                for j in pointList:
                    if (i.distanceTwoDots(j) < closestPair.distance and i != j):
                        closestPair.p1 = i
                        closestPair.p2 = j
                        closestPair.distance = i.distanceTwoDots(j)


    return closestPair



def calculateClosest(pointList):  # bidang pembatas ditengah (x, 0, 0)

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
    
    # REKURENS
    else:
        middle = len(pointList) // 2

        closestPair_Right = calculateClosest()

    
    

points = randomSorted(3)

for i in range(3):
    points[i].displayDot()

closestPair = calculateClosest(points)

print("\nClosest Pair: ")
closestPair.p1.displayDot()
closestPair.p2.displayDot()
print(closestPair.distance)

closestPairBruteForce = bruteforceClosest(points)
print("\nClosest Pair Brute Force: ")
closestPairBruteForce.p1.displayDot()
closestPairBruteForce.p2.displayDot()
print(closestPairBruteForce.distance)
