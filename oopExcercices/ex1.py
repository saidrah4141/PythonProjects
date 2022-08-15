'''
Created on Aug. 10, 2022

* Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

@author: Said
'''

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
