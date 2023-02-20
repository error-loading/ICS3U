fold = 0
thick = 0.1

while thick <= 238900 * 1.6 * 1000000:
    fold +=1
    thick *= 2

print(f"It would take {fold} folds to reach the moon")