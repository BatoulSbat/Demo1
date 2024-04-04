# Define the number of rows for the pattern
num_rows = 5

# Iterate through each row of the pattern
for i in range(1, num_rows * 2):
    # Calculate the number of stars for the current row
    if i <= num_rows:
        stars = i
    else:
        stars = num_rows * 2 - i

    # Print the stars for the current row
    print('*' * stars)
