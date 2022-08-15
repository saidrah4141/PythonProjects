'''
Created on Aug. 11, 2022

*Define a property that must have the same value for every class instance (object)

@author: Said
'''


'''

class Vehicle:

    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color= color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass



bus1 = Bus("School Volvo" , 180 ,12)
audi = Car("Audi Q5" , 240, 180)
print("Color: " , bus1.color, "Vehicle name: " , bus1.name , ", speed: ", bus1.max_speed, ", Mileage: ", bus1.mileage)
print("Color: ", audi.color, "Vehicle Name: " ,  audi.name,  ", Speed: "  , audi.max_speed,  ", Mileage: ",  audi.mileage)
'''

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)