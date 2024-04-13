#encapculation

"""
Public access: Public variables can be accessed by any part
colour variable and start method can be accessed by any part
"""
class Car:
    colour = "red" #public

    def start(self):
        print("Car started")

"""
Private variables and methods can only be accessed within the class
written with double underscores (__)

Protected access can be accessed by the class and the subclasses 
written with single underscore (_)
"""
class Car:
    __engine_capacity = 2000 #private
    _milage = 0 #protected

    def __start_engine(self):
        self.__mileage += 10
        print("Engine started")

#example1
class Person:
    _name = "John" #private variable, change to protected, cuz if is stays private it will give error

    def _greet(self): #private method, change to protected, cuz if is stays private it will give error
        print("Hello, my name is ", self._name)

#create an instance of the class Person
p1 = Person()
# p1._name
# p1._greet()

#polymorphsim and inheritance
class Bird:
    def intro(self):
        print("There are many species of birds.")

    def flight(self):
        print("Most birds can fly but some cannot.")

#inheritance
class Robin(Bird):
    def flight(slef):
        print("Robins can fly!")
        
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly!")

bird = Bird()
bird_robin = Robin()
bird_ostrich = Ostrich()

bird.intro()
bird.flight()

bird_robin.intro()
bird_robin.flight()

bird_ostrich.intro()
bird_ostrich.flight()

#abstraction
from abc import ABC #abstractmethod

class Car(ABC):
    def mileage(self):
        pass