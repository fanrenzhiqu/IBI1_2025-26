# 4.1 Some simple math

a = 5.08
b = 5.33
c = 5.55

# population change
d = b - a
e = c - b

print(d)
print(e)

# Compare growth rates
if e > d:
    print("Population growth is accelerating.")
elif e < d:
    print("Population growth is decelerating.")
else:
    print("Population growth is constant.")

# Comment: d = 0.25 and e = 0.22, so the population growth is decelerating.





# 4.2 Booleans

X = True
Y = False

W = X or Y

print(W)

# Truth table for OR
# X     Y     X or Y
# True  True  True
# True  False True
# False True  True
# False False False

