#static method
class Year:
    @staticmethod
    def is_leap(year):
        """ is_leap is a static method, does not depend on any instance
        specific data, It is an utility function
        check if the year is a leap year
        % is for moduler
        """

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
        
year = int(input("Please input the year "))

if Year.is_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
