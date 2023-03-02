from random import randint
friends = ['bob', 'gary', 'jack', 'person', 'noName']
emotions = ['hates', 'is', 'loves', 'slaps']

ind1 = randint(0, len(friends) - 1)
ind2 = randint(0, len(friends) - 1)
ind3 = randint(0, len(emotions) - 1)

print(f"{friends[ind1]} {emotions[ind3]} {friends[ind2]}")