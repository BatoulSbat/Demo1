#example class
#__init__ is a bulid in function (constructor) to assign values to object properties
#self parameter is a reference to the current instance of the class, It is used to access variables that belong to the class
class Cat:
    def  __init__(self, name = "Fluffy", age = 6, colour = "Black"):  #name, age, colour are attributes
        self.name = name
        self.age = age
        self.colour = colour

    def speak(self):
        """this method speak returns a string with the name of the object
        """
        print(f"{self.name} says Meow!")

    def describe(self):
        """prints description of the cat
        """

        print("My name is %s, I am %d years old and have %s fur. \n" %(self.name, self.age, self.colour)) #%s (for string), %d (for integer) are for the default values
            #%f is for float
            #we also can use the f string method, print(f"My name is {name}, I am {age} years old and have {colour} fur. \n" %(self.name, self.age, self.colour))

#create an object p1 and print value of x
cat1 = Cat("Mrs Norris", 10, "Orange")

#getting all the attributes: cat1.__dict__
print("Ths attributes of the class Cat is: ", list(cat1.__dict__))
print("The attributs values of Cat 1 are: ", list(cat1.__dict__.values()))


# cat1.speak()
# cat1.describe()

#class inheritance, create new lion (child class) based on cat (parents class).
class Lion(Cat):
    """Lion inherits all properties of Cat, but we can override functions, or add new ones
    """

    def __init__(self,name):
        """Makes a lion"""

        self.name = name
        self.age = 4
        self.colour = "Yellow"

    def speak(self):
        """Lions don't meow, they roar, that's why we need to override 'speak' in cat class
        """

        print("Roar!")

cat1.speak()
cat1.describe()

simba = Lion("Simba")

simba.speak()
simba.describe()

#############additional examples
# cat2 = Cat("Sylvester")
# cat3 = Cat()

# print(cat2.name)
# print(cat2.age)
# print(cat2.colour)

# cat_name = input("What is your cat's name? ")
# cat_age = int(input("How old is your cat? "))
# cat_colour = input("What is your cat's colour? ")

# my_cat = Cat(cat_name, cat_age, cat_colour)

# print(f"My cat's name is{my_cat.name}")


