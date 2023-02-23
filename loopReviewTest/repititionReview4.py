# Write a program that gets a number from the user and displays all factors of that number.
# Date: Feb 23, 2023
import math

num = int(input("Enter a number: "))
factors = [(i, num // i) for i in range(1, math.ceil(num ** 0.5)) if not num % i]
print(*factors)