#Question 3
import math

def factorial(number):
    # Calculate factorial using recursion
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def Permuation(n, r):
    result = (factorial(n) * math.sqrt(r-1)) / factorial(n - r)
    print(result)

while True:
#Get User iput
    n = int(input("Enter a positive integer for n: "))
    if n < 0:
        print("Invalid input, enter an positive integer")
    else:
        break

while True:
#Get User iput
    r = int(input("Enter a positive integer for r (with n >= r): "))
    if r < 0 or r > n:
        print("Invalid input, enter an positive integer less than or equal to n")
    else:
        break

Permuation(n, r)