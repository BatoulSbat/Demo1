# #example 1, indexing
# #string list
# my_pokemon = ["squirtle", "metapod", "picachy", "charizard", "genger"]

# #number list
# number_list = [12, 34, 56, -100, 12.4, -1]

# #mixed list
# mixed_list = [[12,34,], "apple cider vinegar", 12, True]
# #                 0                 1          2    3
# # mixedlist[0] = [12, 34]
# #                  0   1
# # mixedlist[0][1] = 34 

# #indexing second value within first list
# print(mixed_list[0][1]) #accessing a list within another list

# #getting last bool value
# print(type(mixed_list[-1])) #checking the type of an element in the mixed list

# #index a word or character within list
# print(mixed_list[1][1]) #withh return the second character in string

# #grabbing string
# print(mixed_list[1])

# #splitting string up by common character
# print(mixed_list[1].split(" "))

# #indexing split up word (list) to access the word 'cider'
# print(mixed_list[1].split(" ")[1])

# #it does not modify the original list
# print(mixed_list)

# my_pokemon = ["squirtle", "metapod", "picachy", "charizard", "gengar"]
# print(my_pokemon)

# my_pokemon.append("garfield")
# print(my_pokemon)

# late_catch = ["venusaur", "slowpoke", "arbok"]
# my_pokemon.extend(late_catch)
# print(my_pokemon)

# my_pokemon.remove("garfield")
# print(my_pokemon)

# imposter_poke = my_pokemon.pop(5)
# print(f"{imposter_poke} has crossed the multi-verse and should not be here")

# print(my_pokemon)

# my_pokemon.pop()
# print(my_pokemon)

# count = 0
# for pokemon in my_pokemon:
#     print(pokemon)
#     count +=1
#     print(count)

#     if pokemon == "gengar":
#         print (f"{pokemon} has been found at position {count}")
#         break

# print(f"value stored inside count is: {count}")
# print(f"the 5th pokemon {count} in the list 'my_pokemon' is: {my_pokemon[count-1]}")

# number_list = [12, 34, 56, -100, 12.4, -1]

#sort() with  numbers
# print("List before sort:")
# print(number_list)

# print("List after sort:")
# #number_list.sort() #sorting in natural order
# number_list.sort(reverse = True) #sorting in reverse
# print(number_list)

# new_sorted_list = sorted(number_list)
# print(number_list)
# print(new_sorted_list)

# #sort() with  words
# my_pokemon = ["squirtle", "metapod", "picachy", "charizard", "genger"]
# late_catch = ["venusaur", "slowpoke", "arbok"]
# my_pokemon.extend(late_catch)
# print(my_pokemon)

# print("List before sort:")
# print(my_pokemon)

# print("List after sort:")
# my_pokemon.sort() #sorting in natural order
# #my_pokemon.sort(reverse = True) #sorting in reverse
# print(my_pokemon)

# #new mixes list
# new_mixed_list = [12, "gengar", 56.78, "slowpoke", True, -3, "ekans"]
# #new_mixed_list.sort()

# #sorted method without unique constraints
# sorted_list = sorted(new_mixed_list, key=lambda x: str(x))

# print(sorted_list)

# print(sorted_list[3])

# print(type(sorted_list[3]))

# #sort() will alter the original list
# #sorted() 

