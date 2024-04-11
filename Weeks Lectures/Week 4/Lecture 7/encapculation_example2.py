#encapculation
class Car:
    """"Car with some speed attribute, accelerate the car, 
    so speed increases, access new speed using a method
    """
    def __init__(self):
        """we use private attribute speed
        """
        self.__speed = 100
    
    def accel(self):
        """increasing the speed attribute of an object by 20
        """
        self.__speed += 20

    def get_speed(self):
        """return the new speed
        """
        return self.__speed
    
#creating an instance of the 'car' class
#it will have its own private speed attribute initialised to 100 when the car object is created

ferrari = Car()

print(ferrari.get_speed())

#this is increasing the speed attribute of the ferrari by 20
ferrari.accel()

#speed was increaed using accel method
print(ferrari.get_speed())














