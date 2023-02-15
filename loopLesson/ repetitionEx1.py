# Create a program that gets the marks the user has for their classes this year.  Tell them how many classes they are failing (despite what many of you think a fail is under 50)
fail = 0

while True:
    mark = int(input("Enter a mark (enter -1 to exit the loop): "))
    if mark == -1: break
    if mark < 50:
        print("You are failing in this course. Try harder!")
        fail += 1 

print(f"You are currently failing {fail} classes")