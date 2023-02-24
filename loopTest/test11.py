cards = int(input("How many cards do you have? "))
pts = 0
if cards <= 7:
    pts = cards
elif cards <= 10:
    pts = cards * 2
elif cards <= 13:
    pts = cards * 3
elif cards <= 15:
    pts = cards * 4
else:
    pts = cards * 5

if pts == 1: print(f"That is {pts} point")
else: print(f"That is {pts} points")