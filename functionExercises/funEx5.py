def knightMove(y, x):
    posMoves = {-2 : [-1, 1], -1 : {2, -2}, 1 : {2, -2}, 2 : [-1, 1]}
    moves = []

    for row in posMoves.keys():
        for col in posMoves[row]:
            if row + x >= 1 and row + x <= 8 and col + y >= 1 and col + y <= 8:
                moves.append((row + x, col + y))
    
    return moves

print(knightMove(7, 4))