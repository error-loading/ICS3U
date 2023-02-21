ttl = 1
cur = 1

while ttl + cur ** 2 < 10000:
    cur += 1
    ttl += cur ** 2

print(f"Leftover: {10000 - ttl}  Layers: {cur}")
# print((30 * 31 * 61) // 6)  -> formula for sum of squares from 1 -> n