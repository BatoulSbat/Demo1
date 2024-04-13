class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #a class method to create a Person object's age by birth year
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, 2024 - year)
    
    #a static methos to check if a Person object is an adult or child
    @staticmethod
    def isAdult(age):
        if age >= 18:
            print("This person is an adult")
        else:
            print("This person is a child")
    
#make a person instance
person1 = Person("Bluey", 7)
#using the class method
person2 = Person.fromBirthYear("Bingo", 2019)

print(person1.age)
print(person2.age)

#using the static method
Person.isAdult(32)


#class method can get back and modify i.e. add 1, while static method can't