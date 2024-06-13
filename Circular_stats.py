"""
Caculate the circular area and circumference.
Print out the result

Author: Jimmy
Date: 03/15/2024

"""
import math

def area(r):
    circular_area = math.pi * r**2
    return circular_area

def circumference(r):
    circular_cirfumference = math.pi * 2 * r
    return circular_cirfumference

radius = float(input("Circular radius: "))

print("Area : "+ str(area(radius))) # <-- Call the area function and print out the result

print("Circumference: " + str(circumference(radius))) # <-- call the circumference function and print out the result



