# There are 3 random function I want you to care about
#  randint
# choice
# shuffle
from random import *

die = randint(1,6) # from 1-6 inclusive
print(die)

nums = [12, 4, 6, 77]
print(choice(nums))  

shuffle(nums)
print(nums)

animals = ["cat", "dog", "rat", "bat", "bee", "elk"]
for i in range(5):   # can repeat
    print(choice(animals))

print("********")
shuffle(animals)
for i in range(5):
    print(animals[i])