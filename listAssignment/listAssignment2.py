# Gurjas Dhillon
# listAssignment2.py
# Names are entered, adds bye to the list if there is an odd number of ppl, output pairings for the tournament

from random import shuffle

names = []
name = input("Enter a name (0 to exit): ")

# whlie loop to enter the names, exits if the user inputs 0
while name != "0":
    names.append(name)
    name = input("Enter a name (0 to exit): ")

# add 'bye' to the tournament if there is an odd number of participants
if len(names) % 2 == 1:
    names.append("Bye")


# shuffle the names list to get them in random order
shuffle(names)


# loop in increments of two to output the names in pairs
for i in range(0, len(names), 2):
    print(f"Match {i//2 + 1}")
    print("-------------------")
    print(f"{names[i]:13} {names[i+1]}\n")
