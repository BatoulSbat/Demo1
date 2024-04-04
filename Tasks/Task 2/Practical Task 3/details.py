#pseudocode
"""
Prompt the user to enter their name
Read the user's input for their name

Prompt the user to enter their age
Read the user's input for their age 

Prompt the user to enter their house number
Read the user's input for their house number

Prompt the user to enter their street name
Read the user's input for their street name

Concatenate all the details into a single sentence
Print the user's details (name, age, house number, street name)
"""

#Prompt the user to enter their name
name = input("Please Enter Your Nanme: ")

#Prompt the user to enter their age
age = input("Please Enter Your Age: ")

#Prompt the user to enter their house number
house_number = input("Please Enetr Your House Number: ")

#Prompt the user to enter their street name
street_name = input("Please Enter Your Street Name: ")

# Concatenate all the details into a single sentence
details_sentence = "This is {}. He is {} years old and lives at house number {} on {}.".format(name, age, house_number, street_name)

# Print out the sentence containing all the details
print(details_sentence)
