n = int(input("Enter a number to calculate its factorial: "))
fact = 1
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, n + 1):
        fact *= i 
    print(f"The factorial of {n} is: ",fact)
