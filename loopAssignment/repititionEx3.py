# Gurjas Dhillon
# repititionEx3.py
# This program outputs a menu, and asks the user for what they would like. It will exit the loop if the user outputs -1. It checks if the user opted to get fries, if not, it asks the user if it would like fries with it. At the end of the program, it outputs the total price

print('''
----HEART ATTACKS ON A BUN -----
1.The Big MOO Combo . . . 5.99
2.Big MOO . . . . . . . . 3.99
3.Spring Surprise . . . . 1.99
4.Fries . . . . . . . . . 1.29
5.Pop . . . . . . . . . . 1.19
6.Exit  --------------------------------
''')
      
menu = {
    1: 5.99,
    2: 3.99,
    3: 1.99,
    4: 1.29,
    5: 1.19
}

fries = False
ttl = 0

user = int(input("What would you like? "))

while user != 6:
    ttl += menu[user]
    if user == 5:
        fries = True
    user = int(input("What would you like? "))

if not fries:
    user = input("Would you like any fries with that [y/n] ")
    if user == 'y':
        ttl += menu[5]

print(f"Your total is ${ttl}")