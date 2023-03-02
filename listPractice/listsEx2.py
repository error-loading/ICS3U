from random import random

fruits = ['apple', 'banana', 'strawberry', 'pie']
prices = []

for i in range(4):
    prices.append(float(str(random() * 10)[:4]))

print(*fruits)
print(*prices)