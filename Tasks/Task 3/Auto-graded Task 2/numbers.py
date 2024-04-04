# Asking the user to enter three different integers and saving them in variables
numbers1 = int(input("Please enter a first  number: "))
numbers2 = int(input("Please enter a second  number: "))
numbers3 = int(input("Please enter a third  number: "))

# Printing out the sum of all the numbers
print(numbers1 + numbers2+  numbers3)

# Printing out the result of subtracting the second number from the first number
print(numbers1 - numbers2)

# Printing out the result of multiplying the third number by the first number
print(numbers3 * numbers1)

# Calculating the sum of all three numbers and printing out the result divided by the third number
sum_numbers = numbers1 + numbers2+  numbers3 #Using a the variable sum_numbers to store the sum
print(sum_numbers / numbers3)