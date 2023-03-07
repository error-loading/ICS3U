import sys

n = int(input("How many people are there in the game? "))
graph = [int(i) for i in input("Enter the names space seperately: ").split()]
visited = []
prev = graph[0]

for i in range(n):
    if prev in visited:
        print('Invalid')
        sys.exit()

    visited.append(prev)
    prev = graph[prev]

print('Valid')