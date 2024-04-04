# #two ways to create dictionary
# #1st way
# car_dict = {
#     "brand": "VW",
#     "model": "Polo",
#     "year": 2018, 
#     "year": 2024 # it will give the second value
# }
# print(car_dict)

# #2nd way 
# car_dict1 = dict(brand = "VW", model = "Polo", year = 2018)
# print(car_dict1)

# for x in car_dict.keys(): 
#     print(x)

# for x in car_dict.values(): 
#     print(x)

# for x in car_dict.items(): 
#     print(x)

# #add new items
# x = car_dict.keys()
# print(x)

# car_dict["colour"] = "red"
# print(x)

# print(car_dict)

# #changing value 
# y = car_dict.values()
# print(y)

# car_dict["model"] = "Golf"
# print(y)

# print(car_dict)

# #to check if key is present
# if "model" in car_dict:
#     print("Yes, 'model' is one of the keys in this dictionary. ")

# print(car_dict)

# #deleting an item from a dictionary
# car_dict.pop("colour") 
# #del car_dict["year"]   #this will also work to delete an item
# #clear is to clear the whole dictionary
# print(car_dict)

# #nasted dictionaries
# car_dict2 = dict(brand = "Hyundai", model = "i30", year = 2020)

# car_dict3 = {"brand": "Hyundai", "model": "Civic", "year": 2019}

# car_list = {"car1": car_dict, "car2": car_dict2, "car3": car_dict3}

# print(car_list)

# print(car_list["car2"])
# print(car_list["car2"] ["model"])