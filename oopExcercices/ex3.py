'''
Created on Aug. 10, 2022

*Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

@author: Said
'''


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
'''
class Bus(Vehicle):
        def details(self):
         print("Name: " ,self.name, " Speed: " , self.max_speed, "Mileage: " ,self.mileage)

schoolBus = Bus("school volvo", 180, 12)
schoolBus.details()
'''


class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)