#with parameter & return statement
def add(num1, num2): #parameter
    """this function returns the sum of num1 and num2"""
    num3 =  num1 + num2 #local variable
    return num3

sum_value = add(10, 20)
print(sum_value)

print(add(20, 30)) #different way of showing the output
print(add(2, 430))
print(add(5, 130))  

#without parameter
def greet():
    print("Hi, my name is Luke.")

greet()

#without parameter
def greet_1(a):
    print(f"Hi, my name is {a}.")

greet_1("Leia")

#f-string with a built-in function
random_text = input("What is your favourite food? ")
print(f"We are out of {random_text} today!")

print(f"Length of user input: {len(random_text)} \n Sorry, that you cannot eat {random_text} today.") #len gives the length of the input

#for example
def my_function(cars):
    for x in cars:
        print(x)

cars = ["Polo", "x-trial", "Jazz"]

print(cars)
my_function(cars)