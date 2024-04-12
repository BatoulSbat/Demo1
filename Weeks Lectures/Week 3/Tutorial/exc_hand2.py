# #typeerror
# try:
#     add_items = 4 + "34"
# except TypeError as e:
#     print(f"Error: {e}")

# #valueerror
# try:
#     int("we are the world")
# except ValueError as e:
#     print(f"This is a ValueError: {e}")

# #nameerror
# try:
#     print(sub_value)
# except NameError as e:
#     print(f"Error: {e}")

# #indexerror
# list1 = [1,2,3,4]
# try:
#     print(list1[4])
# except IndexError as e:
#     print(f"Error: {e}")

# #keyerror
# poke = {"p": "pekatchu", "c": "charizard", "s": "slowpoke"}
# try:
#     print(poke['j'])
# except KeyError as e:
#     print(f"The key  'j' does not exist in the dictionary . Error: {e}")

# #filenotfounderror
# try:
#     with open("lyr.txt", "r") as file:
#         content = file.readline()
# except FileNotFoundError as e:
#     print(f"Error: {e}")
    
# #IOerror


# # #attributeerror
# string1 = "Mangos"
# string1.append("for sale")

# #zerodivisionerror 12/0

# #keyboardinterrupt
# try:
#     while True:
#         print("Hello")
# except KeyboardInterrupt:
#     print("Exterminate!")


# print("This is the end.")
