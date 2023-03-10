# Gurjas Dhillon
# listAssignment4.py
# this program checks if the assasin round is valid or invalid

import sys

n = int(input("How many people are there in the game? "))
graph = [int(i) for i in input("Enter the names space seperately: ").split()]      # get the graph space separelty and use list comprehension to put it in a list right away 
visited = []         # visited list, if the current node is already in this list, then its an invalid round
prev = graph[0]        # variable for the last node visited

for i in range(n):
    # if the prev node is in the visited array, then its an invalid round and it exits the program
    print(prev, i)
    if prev in visited:
        print('Invalid')
        sys.exit()
    
    # if the prev node is index out of range, then its an invalid round and it exits the program
    if prev > n:
        print('Invalid')
        sys.exit()

    # append the prev node into the visited array and update the prev variable
    visited.append(prev)
    prev = graph[prev]

print('Valid')