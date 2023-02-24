name = input("Enter your name: ")

i = 1

while name != "end":
    sec = " " + name
    print(f"Hey{sec * i}!")
    i += 1
    name = input("Enter your name: ")