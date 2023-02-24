# Gurjas Dhillon
# repititionEx5.py
# This program finds how many square based cannonballs u can have if you only have 10000 cannonballs

ttl = 1
cur = 1

# the sentinal is ttl + cur ** 2 < 100000 since u want it to be stricly less than 10000
while ttl + cur ** 2 < 10000:
    cur += 1
    ttl += cur ** 2

print(f"Leftover: {10000 - ttl}  Layers: {cur}")
# print((30 * 31 * 61) // 6)  -> formula for sum of squares from 1 -> n