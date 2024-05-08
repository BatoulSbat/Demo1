# Open the DOB.txt file and read its contents
with open("DOB.txt", "r") as file:
    lines = file.readlines()

# Initialise lists to store names and birthdates
names = []
birthdates = []

# Iterate through each line of the file
for line in lines:
    # Split the line into name and birthdate using any whitespace characters
    data = line.strip().split()
    
    # Check if the line contains "... etc." entry
    if "... etc." in line:
        # Append "... etc." to both names and birthdates lists
        names.append("... etc.")
        birthdates.append("... etc.")
    else:
        # Join the name if it contains multiple parts
        name = ' '.join(data[:-3])
        # Join the birthdate if it contains multiple parts
        birthdate = ' '.join(data[-3:])
        
        # Append name and birthdate to their respective lists
        names.append(name)
        birthdates.append(birthdate)

# Print names
print("Name")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
