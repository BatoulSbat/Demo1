# #string
# name1 = "Linda"
# song = "The Bird Song",
# license_plate = "CTA 456 GP"

# name2 = "John"
# joke = "Knock, Knock who's there"

# #multi-line string
# long_string = ''' This is a long string 
# using triple qoutes preserves everything inside it as a string 
# even on different lines and with different \n spacing. '''

# name3 = "Peter"
# surname = "Parker"
# full_name = name3 + surname
# full_name = name3 + " " + surname #to put space  between names

# print(full_name + str(32)) #when printing two or more than two variables, they have to be converted to one datatype

# #.format
# name4 = "Peter Parker"
# age = 32
# sentence = "my name is {} and I am {} years old." .format(name4, age) 
# """we don't have to convert a variable that contains a number (age) 
# to a string when we use the format method. """
# print(sentence)

# #f-string
# name5 = "Peter Parker"
# age = 32
# sentence = f"My name is {name5} and I am {age} years old."
# print(sentence)

# telephone_num = "041 123 1234"

# #length
# print(len("Hello World!"))

# #slicing
# greeting = "Hello"
# print(greeting[1:4]) #from index 1 till before index 4
# print(greeting[-4:-1]) #from  fourth last char till second last char
# print(greeting[1:]) #from index 1 till end of string
# print(greeting[:4]) #from start till index 4, and  not including 4th index
# print(greeting[1::3])  #start from index 1 and take every third element
# print(greeting[4:1:-1]) #reverse string, begins form  4 ends at 1 (not included), steps  -1 each time 
# print(greeting[::-1]) #this way you can reverse any string, 

# #slicing does not  modify original string but returns new one
# new_string = "Hello World!"
# fizz = new_string[0:5]

# print(fizz)
# print(new_string)

# #float
# x = float(15.20)
# y = float(-32.54e100) # wherer e indicate the power of 10
# print(x, y)

# #complex
# c = complex(45.j)
# print(c)

# class_list = 25 #integer
# interest_rate = 12.23 #float

# num1 = 12
# num2 = 99.99
# print(float(num1))
# #converting floats to ints, as below, causes data loss. int() removes values after the decimal point, returning only a whole number.
# print(int(num2))

# #arithmetic (calculations)
# sum = 2 + 4
# print(sum)

# cents = 0.25 + 4.33
# print(cents)

# sub = 10 - 7
# print(sub)

# #built_in functions
# #round
# number = 66.6564544
# print(round(number, 2))

# #min, max, sum
# numbers_list = [6, 4, 66, 35, 1]
# print(min(numbers_list))
# print(max(numbers_list))
# print(sum(numbers_list))

# import math

# number2 = 30.3333
# print(math.floor(number2))
# print(math.ceil(number2))
# print(math.trunc(number2))
# print(math.sqrt(number2))
# print(math.pi)

# #If statement
# num = 10
# if num < 12: #the colon is important
#     print("The variable number is less than 12")

# num1 = int(input("Please enter a number between 0 and 100: "))
# if num1 < 12:
#     print("The variable number is less than 12")

# #copmarision operations
# # == equal to, > greater than, < less than, ! not
# # >=  greater or equal to, <= less or equal to, != not  equal to
    
# #boolean
# pass_word = False
# pass_word = True

# #if rain: means that if rain == True, because the default  value for boolean variables is True
# umbrella = "Leave me at home"
# rain = False
# if rain:
#     umbrella = "Bring me with"
# print(umbrella)

# #if-else  statements
# num2 = int(input("Please enter a number between 0 and 100: "))
# if num2 < 12:
#     print("The variable number is less than 12")
# else:
#     print("The variable number is more than 12 ")

# #if elif else statements
# # we can have one if and one else and  many elifs
# num3 = int(input("Please enter a number between 0 and 100: "))
# if num3 < 12:
#     print("The variable number is less than 12")
# elif num3 > 13:
#     print("The variable number is more than 13")
# elif num3 < 13:
#     print("The variable number is less than 13")
# else:
#     print("The variable number you entered is 13")

# #another example
# current_time = 12
# if current_time < 11:
#     print("Time for a short jog - let's go!")
# else:
#     print("It's after 11 - it's time for lunch.")

# #another example
# hour = int(input("Please enter what time it is now: "))
# if hour < 18:
#     greeting = "Good day"
# elif hour < 20:
#     greeting = "Good evening"
# else:
#     greeting = "Good night"
# print(greeting)

# #comparing strings
# my_name = "Tom"
# if my_name == "Tom":
#     print("I was looking for you")

# #comparing numbers
# num1 = 10
# num2 = 20
# if num1 >= num2:
#     print("It's not possible that 10 is bigger than or equal to 20")
# elif num1 <= num2:
#     print("10 is less than or equal to 20")
# elif num1 != num2:
#     print('''This is also true since 10 isn't equal to 20, but the elif statement before comes first and is true, so Python will execute 
#           that and never get to this ones''')
# elif num1 == num2:
#     print("Will never exeute this print statement... ")

#logical operation
# and both conditions need to be true, or at least one condition needs to be true, not the statement is true if the condition is false

# #and example
# team1_score = 3
# team2_score = 2
# game = "Over"
# if (team1_score > team2_score) and (game == "Over"):
#     print("COngratulations Team 1, you have won the match!")

# #or example
# speed = int(input("How many kilometers per hour are you travelling at? "))
# belt = input("Are you wearing a safety belt? ")
# if (speed > 80) or (belt != "Yes"):
#     print("Sorry Sir, but I have to give you a traffic fine.")

#equals i.e. n = 7, plus-equals i.e. n +=1 or n = n + 1, minus-equals i.e. n -= 1 or n = n - 1. 
