from math import pi

def getArea(radius) :
    return pi * (radius ** 2)

def getDistance(delay) :
    return 340 * delay

#print(getArea(5))

#print(f"{getDistance(int(input("delay ? : ")))}m")

string = "QWERASDFZXCV"

print(string[0:12:2])