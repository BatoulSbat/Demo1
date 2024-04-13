class Animals:
    #class attribute
    home = "Kruber"

    #creating instance attributes
    def __init__(self, species, age):
        self.species = species
        self.age = age

    #craeting class method
    def animals_home(cls, home):
            cls.home = home

    #instance method
    def insta_method(self):
            #modify the class attribute
            self.home = "Sabi Sands"
            return f"Species: {self.species}, Age: {self.age}, Location: {self.home}"
        
    #static method
    @staticmethod
    def check_age(age):
        if age > 5:
            return "Adult"
        else:
            return "Not Adult"
            
#creare Animal instances
a1 = Animals("Lion", 4)

print(a1.insta_method())
print(a1.check_age(4))