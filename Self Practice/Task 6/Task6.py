# #function
# def add_one(x): #function called add_one has one parameter, x
#     y = x + 1
#     return y

# #calling a function
# result_num = add_one(5) #create a variable and set it to the value returned by the function. when the function is called, 5 is passed in as an argument.
# #the function that you're calling adds one to the argument (so 5+1) and returns 6 which is assigned to the variable result_num

# print(result_num) #print 6

# num_plus_one = add_one(10) #the rsult that the 'add_one' function returns is stored in the num_plus_one variable
# print(("10 plus 1 is equal to: " + str(num_plus_one)+ "."))

# #or even 
# num = 10
# print(("10 plus 1 is equal to: " + str(num_plus_one)+ ".")) #note that you can call the function and print out the result as a single code statemnet, with
# #the call to the print function actually included as one of the arguments.

# print (y) # prints the resulting value while the function is running rather than returning it to be printed later

# add_one(3) #call the add_one function with 3 passed in as an argument. the function that you're calling adds one to the argument (so 3+1) 
# #and prints out the result. it does not return anything at all.

# #scope
# def adding(a, b):
#     total = a + b
#     return (description + str(total)) #access the internal variable, total, but also the external variable, description, which is part of the main
# #code and not part of the function itself.

# x = 2
# y = 3
# description = "Total: "

# sum = adding(x, y)
# print(sum)

# #scope
# def adding(a, b):
#     total = a + b
#     description = "Total: "
#     return (description + str(total))

# x = 2
# y = 3

# sum = adding(x, y)
# print(description + sum) #nameerror

# #default values
# def multiply(num1, num2 = 5): #sets a default value of 5 for num2.
#     total = num1 * num2
#     print(f"{num1} * {num2} = {total}")

# times_5 = multiply(6) #only passes argument into the funtion. because the second parameter has been given  a default value., the function call 
# #will still work - the 6 will be passed in as a num1 and the default 5 will be used as num2.

# def multiply(num1, num2): 
#     total = num1 * num2
#     print(f"{num1} * {num2} = {total}")

# times_5 = multiply(6) #typeerror

# def multiply(num1, num2 = 5): 
#     total = num1 * num2
#     print(f"{num1} * {num2} = {total}")

# times_7 = multiply(6, 7) #typeerror
# times_9 = multiply(num2 = 6, num1 = 9)

# def multiply(num1 = 6, num2 = 5): #both parameteres have default arguments
#     total = num1 * num2
#     print(f"{num1} * {num2} = {total}")

# multiply_test = multiply() #if you provide no arguments both defaults are used
# multiply_test= multiply(1) #if you provide one argument it goes into the first variable and overwrites the 6
# multiply_test= multiply(2, 7) #providing two arguments fills them out from left to right
# multiply_test= multiply(num2 = 8, num1 = 7) #providing  keyword arguments allows you to specify which variables get filled
# multiply_test= multiply(num2 = 8, 7) #specifying one argument and leave the other, will give an error. you have to specify either all or none.