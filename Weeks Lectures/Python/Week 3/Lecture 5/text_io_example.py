#explicit method, relative path, can use absolute path
# jedi = open('list_of_jedi.txt', 'r') this will give an error as the file list_of_jedi.txt does not exist 

file = open('list_of_jedis.txt', 'r')
file.close()

#implicit method, read contents of the file
with open('list_of_jedis.txt', 'r') as file:
    file_content = file.readlines()
    print(file_content)

#reading all lines
    for line in file_content:
        print(line)

#reading specific lines
    first_line = file_content[0]
    print(f"The first line is: {first_line}")

    second_line = file_content[1]
    print(f"The second line is: {second_line}")

    file.seek(0) #this will take you to the first line
#read content
    content = file.read()
    print(f"\nThis is the read output: {content}") # this gives the same result as "print(content)". It's just another way 
    #print(content)

    file.seek(0)
#read line
    content = file.readline() #this will read the first line
    print(f"\n This is the readline() output: ")
    print(content)

#writing to a file
with open('jedi.txt', 'w') as file:
    user_jedi = input("what is your jedi name? ")
    file.write(f"\n{user_jedi}")

    jedi_list = ["Luke", "Rey", "Obi-Wan"]
    bad_list = ["Anakin", "Dooku"]
    file.writelines(bad_list)

    for line in jedi_list:
        file.write(f"\n{line}\n")

#file handling
file = open('jedi.txt', 'rt') #text (t), bin (b)  
print(file.readline())

for x in file:
    print(x)


#appendind mode
f = open ('jedi.txt', 'a')
f.write('Now the file has more content.')
f.close()

f = open('jedi.txt','r') 
print(f.read())

f = open('filename.txt', 'x') #'x' means exclusive, it checks if the file exists or not before creating it.

#removing a file
import os 
os.remove('filename.txt')

#check if file exist and the delete it
if os.path.exists('filename.txt'):  
    os.remove('filename.txt')
else:
    print("The file does not exist")    

#overwrite the content
f = open ('jedi.txt', 'w')
f.write('Oops, I have deleted the content')
f.close()