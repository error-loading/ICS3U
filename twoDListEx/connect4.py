def get(grd, x, y):
    if 0<= x < len(grd) and 0<= y < len(grd[x]):
        return grd[x][y]
    return None

def connect4(lst):
    offset = [(0, 1), (1, 0), (1, -1), (1,1)]

    for x in range(7):
        for y in range(7):
            for dx, dy in offset:
                if get(lst, x + 0*dx, y + 0*dy) and get(lst, x + 1*dx, y + 1*dy) and get(lst, x + 2*dx, y + 2*dy) and get(lst, x + 3*dx, y + 3*dy) and get(lst, x + 0*dx, y + 0*dy) == get(lst, x + 1*dx, y + 1*dy) == get(lst, x + 2*dx, y + 2*dy) == get(lst, x + 3*dx, y + 3*dy):
                    return True
    
    return False

board1 = [[0,0,0,0,0,1],
          [0,0,0,0,1,1],
          [0,0,0,1,1,1],
          [0,0,0,0,0,2],
          [0,0,0,2,2,2],
          [0,0,0,0,0,2],
          [0,0,0,0,0,0]]

board2 = [[0,0,1,1,1,1],
          [0,0,0,2,2,2],
          [0,0,0,0,0,2],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]

board3 = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,2,1,2,1],
          [0,0,0,2,1,1],
          [0,0,0,0,2,1],
          [0,0,0,0,0,2]]

board4 = [[0,0,0,0,0,0],
          [0,0,0,0,0,2],
          [0,0,0,0,2,1],
          [0,0,0,0,2,1],
          [0,0,0,0,2,2],
          [0,0,0,0,2,1],
          [0,0,0,0,0,1]]

print(connect4(board1))  # False
print(connect4(board2))  # True
print(connect4(board3))  # True
print(connect4(board4))  # True
        

