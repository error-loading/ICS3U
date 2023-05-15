fname = input("Class Name: ").strip()

txt = open(f"./fileioEx/{fname}.txt", "w")

for i in range(10):
    txt.write(str(i) + "\n")

txt.close()