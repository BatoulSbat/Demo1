# Asking the user to enter a sentence and saving it in the variable str_manip
str_manip = input("Please enter a sentence: ")

# Calculating and displaying the length of str_manip
print(len(str_manip))

# Displaying the last letters of the entered sentence
print(str_manip[-1])

# Finding the last letter in str_manip and replacing every occurrence of this letter with '@'
replacement = str_manip.replace(str_manip[-1] , "@")
print(replacement)

# Printing the last three characters in str_manip backwards
backward = str_manip[-1:-4:-1]
print(backward)

# Creating a five-letter word made up of the first three characters and the last two characters in str_manip
made_up1 = str_manip[:3] # Getting the first three characters
made_up2 = str_manip [-2:] # Getting the last two characters
print(made_up1 + made_up2)

