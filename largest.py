a = 10
b = 25
c = 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)