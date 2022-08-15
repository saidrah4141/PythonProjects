'''
Created on Aug. 10, 2022

*Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50.

@author: Said
'''


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):
    def seating_capacity(self):
        return Vehicle.seating_capacity(self, 50)

bus = Bus("bus" , 180,12)
print(bus.seating_capacity())

'''
class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
'''