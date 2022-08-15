'''
Created on Aug. 14, 2022

@author: Said
'''



class Vehicle: 
    def __init__ (self, speed, doors, mileage):
        self.speed = speed
        self.doors = doors
        self.mileage = mileage
    
    def distance(self, time):
        return(self.speed * time)
class bus(Vehicle):
    def distance(self, time):
        return(self.speed)
class car(Vehicle):
    pass

honda = car(180,4,12)
school = bus(180, 1, 8)
print(school.distance(5))
print(honda.distance(5))