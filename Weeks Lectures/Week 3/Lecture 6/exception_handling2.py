def validate_input(value):
    if not isinstance(value, int):
        raise ValueError("Hey, the input must be an integer")
    
try:
    validate_input("Hello World!") 
except ValueError as e:
    print(f"Error: {e}")

#example2
def add_num(n1, n2):
    if not (isinstance(n1, (int, float)) and isinstance(n2, (int, float))):
        raise ValueError("Both numbers n1 and n2 should be either integer or float.")
    return n1+n2

print(add_num(1, 'str'))

print("This is the end. ")


#enclose calling the function in a try except block
try:
    print("This sum is: " ,add_num(20, "56"))
except ValueError as e:
    print(f"Error : {e}")


#print("This is the end")    

#try (if else) except
try:
    var1 = int(input("Enter the number of muffins stolen: "))
    print(f"Godh!, {var1} muffins! that's a lot for sure!")
except ValueError:
    print("muffins are whole items, please enter an integer value, e.g. 42")
except NameError as e:
    print(f"Error: {e}")

while True:
    try:
        order1 = int(input("How many muffins do you want? "))
        if order1 >= 1:
            print(f"You have ordered {order1} muffins. Enjoy your day!")
        else:
            print("You have not ordered any muffins. Good bye! ")
        break #without the break  statement the loop will run infinitely
    except ValueError:
        print("You cannot have fractional muffins. Please enter an integer value.")