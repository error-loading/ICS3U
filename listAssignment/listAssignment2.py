from random import shuffle

names = []
name = input("Enter a name (0 to exit): ")

while name != "0":
    names.append(name)
    name = input("Enter a name (0 to exit): ")

if len(names) % 2 == 1: names.append("Bye")

shuffle(names)

for i in range(0, len(names), 2):
    print(f"Round {i//2 + 1}")
    print("-------------------")
    print(f"{names[i]:16} {names[i+1]:16}\n")
