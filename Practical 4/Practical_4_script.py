4.1

a=5.08
b=5.33
c=5.55
d=b-a
e=c-b

test_variable = round(c,1)
print(test_variable)
print(d)
print(e)
print(d>e)
if e > d:
    print("Population growth is accelerating.")
elif e < d:
    print("Population growth is decelerating.")
else:
    print("Population growth is constant.")
#comment: 2.5>2.2, so the population growth is decelerating

4.2
X=True
y=False
W=X or Y
print(W)
