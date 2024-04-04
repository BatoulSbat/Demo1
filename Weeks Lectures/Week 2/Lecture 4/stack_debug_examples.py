# #example 1: division by 0
# def divide (num1, num2):
#     print(num1/num2)

# # divide(10,0) # will cause an error because you can't divide a number by zero
# divide(10,0.001)

# #name error
# name = "Luke"
# #print('Hello, ' + nam)   #NameError: name 'nam' is not defined
# print('Hello, ' + name)

# #syntax error
# #def say(name) #syntax error: missing colon at the end of function definition
# def say(name):
#     print("Hello, " + name)

# say("Luke")

# #type error
# #sum_value = 45 + "tree" #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum_value = str(45) + " tree"
# print(sum_value)

# #example #type error or syntax error
# # a = (1,20,18) 
# a = [1,20,18]
# a [2] = 30
# print(a)
# print(len(a))

# #example index error
# #print(a[3]) #out  of range; list index out of range
# print(a[2])

# #attribute error, import error, value error, key error, index error, IO error. (key error, index error are for dictionary)

# #debug 
# x = 0
# while x > -5:
#     print(x)
#     x -= 1
#     # to exit the infinit loop, control + c

# #adds sum of 0 to n
# def addsum(n):
#     total = 0
#     for i in range(n+1): #range(n) means 0,1,2,3. ......, n-1, n+1 is to include the number 5
#         total += i
#     return total
    
# print(addsum(5))

# #adds sum of 0 to n
# def addsum(n):
#     total = 0
#     for i in range(n): #range(n) means 0,1,2,3. ......, n-1 
#         print (i) #additional print statement for intermediate value
#         total += i
#         return total
    
# print(addsum(5))

