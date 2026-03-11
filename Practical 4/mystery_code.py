# What does this piece of code do?
# Answer:
# This code generates a random integer between 1 and 10 using randint()in each iteration of the loop and adds it to total_rand.
# The loop runs 11 times (progress starts at 0 and continues while progress <= 10), then prints the final sum.
# The ceil() function is imported but not used.

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

