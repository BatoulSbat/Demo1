# Initialise variables
total = 0
count = 0

# Continually ask the user to enter a number until -1 is entered
while True:
    num = float(input("Enter a number (-1 to stop): "))
    
    # Check if the entered number is -1
    if num == -1:
        break  # Exit the loop if -1 is entered
    
    total += num  # Add the entered number to the total
    count += 1    # Increment the count of numbers entered

# Check if any number other than -1 was entered
if count > 0:
    # Calculate the average of the numbers entered
    average = total / count
    print("Average of the numbers (excluding -1) is:", average)
else:
    print("No numbers were entered (excluding -1).")
