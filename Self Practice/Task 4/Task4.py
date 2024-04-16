# #while loop
# sum1 = 0
# i = 2 #initial even integer for the sum

# while sum1 <= 250: 
#      sum1 += i
#      print(i)
#      i += 2 #update statement, shorthand for i = i + 2

# print(sum1)

# #counting up to 10
# i = 0

# while i <= 10:
#      print(i) # Print the current value of the i
#      i += 1 # Increment i by 1 for the next iteration

# #infinite loop
# my_number = 0
# while my_number < 100:
#      my_number += 1
#      print(my_number)
#      if my_number == 23:
#           break

# #continue statement
# my_number = 0
# while my_number < 100:
#      my_number += 1
#      if my_number > 23:
#           continue
#      print(my_number)

# #for loop
# #the function range (start index, end index), the start index is included  and the end index is not included.
# for i in range (1, 10): #i =  1 because it's the first number we want to count from and 10 because we want to go till 9.
#     print(i)

# for  i in range(1, 10):
#     if i > 5:
#         print(i)

# num_list = [1, 2, 3, 4, 5]
# found = False
# num = int(input("Input a number from 1 to 10 and find out if it's in our list: "))
# if num < 1 or num > 10:
#     print("Number out of range")
# else:
#     for number in num_list:
#         if num == number:
#             found = True
#             break
# print(f'List contains {num}: {found}')

# #nasted loop
# for x in range (1, 6):
#     for y in range (1, 6):
#         print(f"{x} * {y} = {x * y}")
# print(" ")
