class Avengers:
    """"
    total_avengers is a class variable to keep track of the total number of avengers

    """
    total_avengers = 0

    def __init__ (self, name):
        """"
        total_avengers: incremet the total number of avengers
        when a new avenger instance is created.
        """
        self.name = name
        Avengers.total_avengers += 1 

    @classmethod
    def display_total_avenger(cls):
        print("the total number of avengers: ", cls.total_avengers)


#create instances of the class avengers
anenger1 = Avengers("Captain America")
anenger2 = Avengers("Iron Man")
anenger3 = Avengers("Black Widow")

#calling the class method to display the total numbers of avengers
Avengers.display_total_avenger()