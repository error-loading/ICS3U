from random import *

out = open("./fileio/nums.txt", "w")

for i in range(1000):
  out.write(str(randint(1, 500)) + "\t")

out.close()