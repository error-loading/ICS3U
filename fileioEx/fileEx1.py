txt = [i.strip() for i in open("./fileioEx/names.txt").readlines()]

for names in txt:
    names = names.split()
    print(f"Hello, {names[0]}")

