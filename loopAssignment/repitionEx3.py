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

order = []
ttl = 0

user = int(input("What would you like? "))

while user != 6:
    order.append(user)
    ttl += menu[user]
    user = int(input("What would you like? "))

if 4 not in order:
    fries = input("Would you like any fries with that [y/n] ")
    if fries == 'y':
        ttl += menu[5]

print(f"Your total is ${ttl}")