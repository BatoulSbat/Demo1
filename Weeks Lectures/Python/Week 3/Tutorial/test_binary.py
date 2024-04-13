# prime_numbers = [2,3,5,7]
# #convert list to binary data using bytearray
# binary_data = bytearray(prime_numbers)

# print('Binary Data: ', binary_data)

# filename = "test.bin"
# #write this binary data in a file
# with open(filename, "wb") as file:
#     file.write(binary_data)

#reading a binary file, explicit
f = open("/Users/BatoulSbat/Desktop/Courses/CoGrammar/Weeks Lectures/Week 3/Lecture 6/test.bin", "rb")
#read file data with read()
data = f.read()
#check what is the type of data
print(type(data))

#print byte sequence data
print(data)

#close opened file
f.close()

