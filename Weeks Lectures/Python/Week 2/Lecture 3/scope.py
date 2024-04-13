#random function
def hogwarts(h1, h2):
    print(f"character 1: {h1}. \n character 2: {h2}")
    print(f"You have an extra character: {third_char}")

third_char = "Hermione" #global variable

hogwarts("Harry", "Ron")


def my_func():
    #default: inside the function, it is a local  variable.
    global y # if this is not global, last statement print(y) won't work
    y = "Here comes the sun"
    print(y)

my_func()

print(y)

