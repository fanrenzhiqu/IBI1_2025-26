# Set the starting number of infected students
number = 5

# Set the daily growth rate
rate = 0.4

# Set the day counter
day = 1

# Display the starting day and infected number
print("Day", day, "- infected students:", number)

# Keep calculating infection numbers until all 91 students are infected
while number < 91:
    # Calculate the next day's infected number
    number = number * (1 + rate)

    # Increase the day count
    day = day + 1

    # Display the infected number for this day
    print("Day", day, "- infected students:", number)

# Report how many days were taken to infect the whole class
print("It took", day, "days to infect the whole class 91 students.")
