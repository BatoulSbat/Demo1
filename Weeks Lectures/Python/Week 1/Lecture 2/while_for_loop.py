#while loop: printing count up tp 4

#example 1
count = 0
while count < 5:
    print (count)
    count +=1
    #count +=1 same as count = count + 1

count = 0
while count <= 5:
    print (count)
    count +=1

#print backward
count = 10 
while count > 0:
    print (count)
    count -=1


# example 2
random_sent = "Hello there General Kenobi"

for letter in random_sent:
    print(letter)

#example 3
poke_list = ["Pikachu", "Charizard", "Genger", "Squirtle"]

for poke in poke_list:
    print("Current Pokemon", poke)

# example 4
#range (start, stop, step)
# start defualt = 0, can skip
# stop required, can't skip
# step default = 1, can skip
# range(6) -> 0,1,2,3,4,5
    
for number in range (0, 10, 2):
    print(number)

for number in range (6):
    print(number)


#example 5
random_sent = "Well, of course I know her. she's me"
random_sent_split = random_sent.split(" ")
print(random_sent_split)

for letter in random_sent_split:
    print(letter)

#example 6
    #print ("this is example 6")
for i in range (1, 4):
    for j in range (1,4):
        print (i*j, end ="") #end ="" means ending with no space
    print ()