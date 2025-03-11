a = input("Enter the first number (a): ")
b = input("Enter the second number (b): ")
c = input("Enter the third number (c): ")
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"The largest number is: ",largest)
