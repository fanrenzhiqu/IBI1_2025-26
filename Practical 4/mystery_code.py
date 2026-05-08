# What does this piece of code do?
# Answer:
# This code generates 11 random integers between 1 and 10 and adds them together.
# It starts with total_rand = 0 and progress = 0.
# The while loop runs 11 times because progress starts at 0 and continues while progress <= 10.
# In each loop, randint(1, 10) generates one random integer, and this number is added to total_rand.
# Finally, the program prints the sum of the 11 random numbers.
# The ceil() function is imported but not used in this code.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

print(total_rand)

