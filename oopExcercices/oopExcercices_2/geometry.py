'''
Created on Aug. 18, 2022


1 - Write a methode in Geometry class called distance() that allow to compute a distance between two points A = (a1, a2), B = (b1, b2) (with the convention: a point M is identified with its pair of coordinates M = ( x, y)).
2 - Write a methode in Geometry class called middle() allowing to determine the midle of bipoint (A,B).
3 - Write method called trianglePerimeter() allowing to compute the perimeter of triangle
4 - Write method called triangleIsoscel() which returns a True if the triangle is isoscel and False if not.

@author: Said
'''
import math
from _ast import Or
from pickle import TRUE
from _operator import or_

class Geometry:
    
    def distance(self, a1,a2,b1,b2):
       c = (a1-b1)**2 + (b1-b2)**2
       distance = math.isqrt(c)
       return(distance)
    def middle(self, a, b):
        midpoint = (a+b)/2
        return(midpoint)
    def triangleIsoscel(self,a,b,c):
        if a == b or a ==c:
            return (True) 
        else:
            return (False)
            
        
shape = Geometry()
print(shape.triangleIsoscel(3,4,3))