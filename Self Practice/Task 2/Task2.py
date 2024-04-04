print("HEllo, World!") #HEllo, World! is the argument

#input
name = input ( "Enter your name: ")   #Asking user to enter their name
print("Hello" + " " + name)         #Printing Hello and a space followed by the users name.

#variable
num = 2 #this is a variable and we assign the number 2 to it 

#datatype
number_str = "10"
print(number_str * 2)             #This will print 1010 because we multiplied a string of numbers by  2
print(int(number_str) * 2)          #This will convert the string into an integer and then multiply it by 2 so it prints 20

#determine the datatype
mystery_1 = "10"
mystery_2 = 10.6
mystery_3 = "ten"
mystery_4 = True

print(type(mystery_1))
print(type(mystery_2))
print(type(mystery_3))
print(type(mystery_4))

#casting (converting one data type to another)
number = 30
number_str = "10"
print(number + int(number_str)) #converting string into integer
print(number_str + str(number)) #converting  integer into string
# print(number_str + number) this will show error as  you can't add string with an integer directly. We need to use casting.

num_days = int(input("How many days did you work this month? "))
pay_per_day = float(input("how much is your pay per day? "))
salary = num_days * pay_per_day
print("My salary for the month is USD: {}". format(salary))
"""when working with strings, we are able to put variable into our strings with the format method. 
to do this, we use curly braces {} as placeholders for our values. then, after the string, we put .format(variable_name). 
when the code runs, the culy braces will be replaced by the value in the variable specified in the brackets after the format method."""

num_days = 28
pay_per_day = 50
print(f"I worked {num_days} days this month. I earned ${pay_per_day} per day.") #f-string is kind of the same as .format method
"""print("You worked {0} days this month and earned ${1} per day". format (num_days = 28, pay_per_day = 50))
 this won't work as we're not passing them as keyword arguments"""
print("You worked {num_days} days this month and earned ${pay_per_day} per day". format (num_days = 28, pay_per_day = 50)) 

