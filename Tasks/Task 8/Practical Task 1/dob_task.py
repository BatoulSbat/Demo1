# Open the DOB.txt file and read its contents
with open("DOB.txt", "r") as file:
    lines = file.readlines()

# Initialise lists to store names and birthdates
names = []
birthdates = []

# Iterate through each line of the file
for line in lines:
    # Split the line into name and birthdate
    name, birthdate = line.strip().split(":")
    
    # Append name and birthdate to their respective lists
    names.append(name.strip())
    birthdates.append(birthdate.strip())

# Print names
print("Name")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
