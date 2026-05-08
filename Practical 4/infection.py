# Pseudocode:
# Start with 5 infected students.
# Set the daily infection growth rate to 0.4.
# Start counting from day 1.
# Print the number of infected students on day 1.
# While the number of infected students is less than 91:
#     Calculate the next day's infected number using the growth rate.
#     Increase the day counter by 1.
#     Print the day number and the infected number.
# Print the total number of days needed to infect the whole class.


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
