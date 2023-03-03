from random import randint

operations = {
    6: 17,
    14: 3,
    20: 15,
    24: 26,
    30: 44,
    39: 33,
    49: 62,
    66: 53,
    69: 58,
    79: 67,
    84: 71,
    88: 36,
    82: 86
}

player1 = 1
player2 = 1

turn = 1


while player1 != 90 or player2 != 90:
    input(f"Player {turn}  hit enter to roll ")
    roll = randint(1, 6)
    print(f"You rolled: {roll}")

    if turn == 1:
        if player1 + roll > 90:
            print("You rolled higher than 90")
        elif player1 + roll in operations:
            if operations[player1 + roll] > player1 + roll:
                print("You climbed a lander")
            else:
                print("Snake")
            player1 = operations[player1 + roll]
            print(f"You are at spot {player1}")
        else:
            player1 += roll
            print(f"You are at spot {player1}")
    else:
        if player2 + roll > 90:
            print("You rolled higher than 90")
        elif player2 + roll in operations:
            if operations[player2 + roll] > player2 + roll:
                print("You climbed a lander")
            else:
                print("Snake")
            player2 = operations[player2 + roll]
            print(f"You are at spot {player2}")
        else:
            player2 += roll
            print(f"You are at spot {player2}")
    
    turn += 1
    if turn == 3: turn = 1