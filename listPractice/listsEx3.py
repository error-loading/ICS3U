kids = []
weeds = []

ttl = 0

for i in range(8):
    name = input("Enter name: ")
    val = int(input("Number of weeds pulled: "))

    ttl += val

    kids.append(name)
    weeds.append(val)

for i in range(8):
    perc = weeds[i] / ttl
    print(f"{kids[i]} gets ${round(100 * perc, 2)}")

