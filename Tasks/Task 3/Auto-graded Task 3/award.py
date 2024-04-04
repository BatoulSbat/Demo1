# Read in the times (in minutes) for swimming, cycling, and running
swim_time = float(input("Enter the time taken for swimming (in minutes): "))
cycle_time = float(input("Enter the time taken for cycling (in minutes): "))
run_time = float(input("Enter the time taken for running (in minutes): "))

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time

# Display the total time taken
print("Total time taken to complete the triathlon:", total_time, "minutes")

# Determine the award based on the total time taken
if total_time <= 100:
    award = "Provincial colours"
elif 100 < total_time <= 105:
    award = "Provincial half colours"
elif 105 < total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

# Display the award the participant will receive
print("Award:", award)
