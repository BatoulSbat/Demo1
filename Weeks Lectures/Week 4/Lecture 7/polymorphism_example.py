class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
def make_noise(animal):
    return animal.sound()
    
my_dog = Dog()
my_cat = Cat()

print(make_noise(my_dog))
print(make_noise(my_cat))