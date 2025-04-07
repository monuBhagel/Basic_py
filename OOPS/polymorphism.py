'''
- Polymorphism is a core concept in OOP that allows objects of different classes to be treated as objects of a common superclass.
- a example of it is the built-in len() function , it can be used with list , string, tuples, dict ,etc.


'''

# example of polymorphism:

class Vehicle :
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(" moving ....")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print(" boat is moving ....")
        
class Plane(Vehicle):
    def move(self):
        print("plane is flying ....")
        
        
# creating objects of each class 

car = Car("Ford", "mustang")
boat = Boat("Boat", "Ship")
plane = Plane("Boeing", "747")

car.move()
boat.move()
plane.move()