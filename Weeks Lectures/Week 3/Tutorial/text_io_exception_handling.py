#modes r, w, a, +, x

#f = open("lyrics.txt", "x")

#x will create a new file, if and only if  it doesn't exist already
#w will create a new file wether or not there is a file with the same name (it will overwrite the file)

#read + write, read + append
filename = 'lyrics.txt'
# r+ opens file for both reading and writing, if file does not exist, an error
# w+ opens file for both reading and writing, text is overwritten

output = input("What line do you want to add? ") #"\nWhat a wonderfull world"
# with open (filename, 'r+') as f:
#     data = f.read()
#     print(data)
#     #add more content in the begining of the file
#     f.seek(0) #this command moves the cursor to the beginning of the file
#     f.write(output)
#     f.truncate() #this command removes all the other characters after what we have written

# a+ apprnding to the original file
with open(filename, 'a+') as f:
    data = f.read()
    print(data)
    f.write(output)
    


