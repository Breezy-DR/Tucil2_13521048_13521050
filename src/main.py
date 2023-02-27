from tool import *
from dotVisualizer import *
from dot import *
from timeit import default_timer as timer

class InvalidN(Exception):
    pass

print("\n\nWelcome to Closest 3D Dot Finder!")
print("\n=============================================\n")

while True:
    n = input("Masukkan nilai n: ")
    try:
        n = int(n)            
    except ValueError:
        print("Nilai n harus berupa integer >= 2. Silakan coba lagi.")
    else:
        try:
            if n < 2:
                raise InvalidN
            else:
                break
        except InvalidN:
            print("Nilai n >= 2. Silakan coba lagi.")

print("\n=============================================\n")

points = randomSorted(n)

startDVC = timer()
closestPairDVC, countDVC = calculateClosest(points)
endDVC = timer()
timeDVC = endDVC - startDVC

startBF = timer()
closestPairBrute, countBrute = bruteforceClosest(points)
endBF = timer()
timeBF = endBF - startBF


print("\n=============================================\n")
print("***DIVIDE AND CONQUER METHOD***")
print("\n=============================================\n")

print("Closest Pair: ")
closestPairDVC.p1.displayDot()
closestPairDVC.p2.displayDot()

print("\n=============================================\n")

print("Pair Distance:")
print(closestPairDVC.distance)

print("\n=============================================\n")

print("The amount of Euclidean operations done:")
print(countDVC)

print("\n=============================================\n")
print("Divide and Conquer algorithm duration: ")
print(f"{timeDVC * 10**6} microseconds")
print("\n=============================================\n")

print("\n=============================================\n")
print("***BRUTE FORCE METHOD***")
print("\n=============================================\n")

print("Closest Pair: ")
closestPairBrute.p1.displayDot()
closestPairBrute.p2.displayDot()

print("\n=============================================\n")

print("Pair Distance:")
print(closestPairBrute.distance)

print("\n=============================================\n")

print("The amount of Euclidean operations done:")
print(countBrute)

print("\n=============================================\n")
print("Brute Force algorithm duration: ")
print(f"{timeBF * 10**6} microseconds")
print("\n=============================================\n")

xOthers, yOthers, zOthers = getSeparateXYZ(points,closestPairDVC)
xClosest,yClosest, zClosest = getSeparateClosestXYZ(closestPairDVC)

plot3D(xClosest,yClosest,zClosest,xOthers,yOthers,zOthers)
