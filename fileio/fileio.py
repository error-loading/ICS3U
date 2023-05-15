# File i/o - input/output
# This is where our program can read from and write to external files
# Input
# read() - reads as one big string
# readline()
# e.g.
# 3
# fr1
# fr2
# fr3
# 2
# loves
# hates
# readlines() - reads the whole file as a list of strings
ttl = 0
fin = open("./fileio/some.txt")
for n in fin.read().split():
    ttl += int(n)
print(ttl)

# print(sum([int(n) for n in open("nums.txt").read().split()]))