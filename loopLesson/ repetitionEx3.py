# Write a program to be used by student council in this upcoming election to tabulate the votes after the election. Your program will list, and number, the three candidates for president then allow the user to enter all of the ballets until they enter 0 then tell them who won the election and what percentage each candidate earned.
cand = {
    "1" : "Sir John A Macdonald",
    "2" : "Alexander Mackenzie",
    "3" : "Sir John Abbott"
}
print('''
1. Sir John A Macdonald
2. Alexander Mackenzie
3. Sir John Abbott
''')
ttlVotes = 0
numVotes = [0, 0, 0]

while True:
    vote = int(input("Enter vote (0 to exit) "))
    if vote == 0:
        break
    numVotes[vote-1] +=1
    ttlVotes +=1

for i in range(3):
    print(f"{cand[str(i+1)]} earned {round(numVotes[i] / ttlVotes * 100, 2)}%")
