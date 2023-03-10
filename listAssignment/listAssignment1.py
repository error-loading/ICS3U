# Gurjas Dhillon
# listAssignment1.py
# A word and its number of points are entered, it later calculates the average score and outputs each word that is below the average

words = {}

word = input("Enter a word (0 to exit) ")

while word != "0":
    pts = int(input("How much does the word worth? "))
    words[word] = pts          # Entering the words with their points in a dictionary
    word = input("Enter a word (0 to exit) ")

ttl = sum(list(words.values()))           # getting the ttl sum of the points

avg = ttl / len(words)         # calculating the avg

for x, y in words.items():      # for each loop 
    # checking if the score for the word is less than the avg
    if y < avg: 
        print(f"The word, '{x}', is below average")
        