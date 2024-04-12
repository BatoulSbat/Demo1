#pseducode: what makes up classes? class for HousePlan
"""
#Attributes
size - sma;;, medium, large
colour - white, blue, red
number of room - 2,3,10
type of flooring - hardwood, carpet, tile

#Methods
opening door
turning on light
cleaning

#Objects will be referred as instances, these would be 
the houses built from the blueprint provided
"""

class HousePlan:
    """"
    This is the class docstring. this class initialised a house object with 
    specified attributes and includes methods for opening doors, turning lights on, and cleaning.

    :param size: Size parameter in the __init__ method of the class to represent the size of the house.

    :para colour: 
    """     

#this is how we initialise our class
    def __init__(self, user_size, user_colour, user_num_rooms, user_floor):
        self.size = user_size
        self.colour = user_colour
        self.num_rooms = user_num_rooms
        self.floor = user_floor

    def openDoor(self):
        """
        This function open door prints a message that a door has been opened
        """
        print("A door has been opened.")

    def lightOn(self):
        print("Light has beed turned on.")

    def houseClean(self):
        print("Rumba claims that the house has been cleaned.")


#user input 
h_size = input("What size house do you want? (small, medium, large) ")
h_colour = input("What colour walls do you want in the house? (white, blue, green) ")
h_num_room = int(input("How many rooms would you prefer? (enter an integer value) "))
h_floor = input("what type of flooring would you like? (wood, tile, carpet) ")

#objects instances
luke_house = HousePlan(h_size, h_colour,h_num_room, h_floor)
leia_house = HousePlan('medium', 'beige', 5, 'wood')

#print result
print(f"""
        Size: {luke_house.size}
        Colour: {luke_house.colour}
        No. of rooms: {luke_house.num_rooms}
        Type of floor: {luke_house.floor}

    """)

leia_house.openDoor()
leia_house.lightOn()
leia_house.houseClean()