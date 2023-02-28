from dot import *
from random import *

def dotSorted(n, dimention):
    # Menghasilkan list point yang terurut berdasarkan nilai sumbu x

    pointList = []

    for i in range(n):
        dot = Dot(dimention)
        pointList.append(dot)

    pointList = sorted(pointList, key=lambda Dot:Dot.coordinates[0])
    
    return pointList

def bruteforceClosest(pointList):

    euclideanCount = 0
    if(len(pointList) > 1):
        euclideanCount += 1
        closestPair = PairOfDots(pointList[0], 
                                pointList[1], 
                                pointList[0].distanceTwoDots(pointList[1]))

        for i in pointList:
                for j in pointList:
                    euclideanCount += 1
                    if (i.distanceTwoDots(j) < closestPair.distance and i != j):
                        closestPair.p1 = i
                        closestPair.p2 = j
                        closestPair.distance = i.distanceTwoDots(j)

    return closestPair, euclideanCount

def minDistancePair(pair1, pair2):
    
    if(pair1.distance < pair2.distance):
        return pair1
    else:
        return pair2
    

def distanceAbscissa(point1, point2):
    # Menghitung jarak dengan memperhatikan atribut x saja
    return abs(point1.coordinates[0] - point2.coordinates[0])



def calculateClosest(pointList):  # bidang pembatas ditengah (x, 0, 0)

    # BASIS 
    countEuclidean = 0
    if(len(pointList) == 2):

        closestPair = PairOfDots(pointList[0], 
                                pointList[1], 
                                pointList[0].distanceTwoDots(pointList[1]))
        
        countEuclidean += 1
        return closestPair, countEuclidean

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
        
        countEuclidean += 3

        return closestPair, countEuclidean
    
    # REKURENS
    else:
        middle = len(pointList) // 2

        closestPair_Right, countRightEuclidean = calculateClosest(pointList[:middle])
        countEuclidean += countRightEuclidean
        closestPair_Left, countLeftEuclidean = calculateClosest(pointList[middle:])
        countEuclidean += countLeftEuclidean

        closestPair = minDistancePair(closestPair_Left, closestPair_Right)

        # EVALUASI BIDANG
        # bidang yang mengandung poin dengan kemungkinan
        # jarak lebih kecil dari closestPair
        pointField = []
        
        for i in pointList:
            if (distanceAbscissa(i, pointList[middle]) < closestPair.distance):
                pointField.append(i)

        for a in pointField:
            for b in pointField:
                countEuclidean += 1
                if (a.distanceTwoDots(b) < closestPair.distance and a != b):
                    closestPair = PairOfDots(a, b, a.distanceTwoDots(b))
        
        return closestPair, countEuclidean

def getSeparateXYZ(pointList, closestPair):
    # Mengembalikan tuple berisi list atribut x, y, z yang terpisah
    # dari titik-titik yang bukan merupakan pasangan titik terdekat
    xs = []
    ys = []
    zs = []
    for i in range (0, len(pointList)):
        if (not pointList[i].isEqual(closestPair.p1)):
            if (not pointList[i].isEqual(closestPair.p2)):
                xs.append(pointList[i].coordinates[0])
                ys.append(pointList[i].coordinates[1])
                zs.append(pointList[i].coordinates[2])
    return xs, ys, zs

def getSeparateClosestXYZ(closestPair):
    # Mengembalikan tuple berisi list atribut x, y, z yang terpisah
    # dari titik-titik yang merupakan pasangan titik terdekat
    xclosest = []
    yclosest = []
    zclosest = []
    xclosest.append(closestPair.p1.coordinates[0])
    yclosest.append(closestPair.p1.coordinates[1])
    zclosest.append(closestPair.p1.coordinates[2])
    xclosest.append(closestPair.p2.coordinates[0])
    yclosest.append(closestPair.p2.coordinates[1])
    zclosest.append(closestPair.p2.coordinates[2])
    return xclosest, yclosest, zclosest



# points = dotSorted(100, 3)

# for i in range(3):
#     points[i].displayDot()

# closestPair, count1 = calculateClosest(points)

# print("\nClosest Pair: ")
# closestPair.p1.displayDot()
# closestPair.p2.displayDot()
# print(closestPair.distance)
# print(count1)

# closestPairBruteForce = bruteforceClosest(points)
# print("\nClosest Pair Brute Force: ")
# closestPairBruteForce.p1.displayDot()
# closestPairBruteForce.p2.displayDot()
# print(closestPairBruteForce.distance)

# xlist, ylist, zlist = getSeparateXYZ(points, closestPair)
# x1, y1, z1 = getSeparateClosestXYZ(closestPair)

# print(xlist)
# print(ylist)
# print(zlist)
# print(x1)
# print(y1)
# print(z1)