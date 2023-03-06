words = {}

word = input("Enter a word (0 to exit) ")

while word != "0":
    pts = int(input("How much is the word worth? "))
    words[word] = pts
    word = input("Enter a word (0 to exit) ")

ttl = sum(list(words.values()))

avg = ttl - len(words)

for x, y in words.items():
    if y < avg:
        print(f"The word, '{x}', is below average")
        