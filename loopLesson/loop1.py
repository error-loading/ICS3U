# e.g. 1
# x = 0
# while x < 20:
#     x = x + 1
#     print(x)


# e.g. 2
# name = ""
# while name != "end":  # "end" is called a sentinel - value that tells us our input is done
#     name = input("Enter name: ")
#     print(f"Hello, {name}")

# e.g. 3
# name = ""
# while True:
#     name = input("Enter name: ")
#     if name == "end":
#         break           # exits the loop that it is inside
#     print("Hello", name)

# e.g. 4 Write a program that gets marks until -1 is entered
# then displays the avg

# ttl = 0        # accumulator - start at 0, add what you are accumulating
# num = 0        # counter - start at 0, add 1 every time your condition occurs
# while True:
#     mark = float(input("Enter mark: "))
#     if mark == -1:
#         break
#     num += 1; ttl += mark

# avg = ttl / num
# print(f"The average is {round(avg, 1)}")


# e.g. 5 - add up all integers from 1 to 100 inclusive
# print((1+100) * 100 // 2)
# print(sum([i for i in range(1, 101)]))

# ttl = 0
# num = 1

# while num <= 100:
#     ttl += num
#     num += 1

# print(ttl)

# e.g. 6 The for loop
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# e.g. 7 - exponential growth and decay
# I invest $5000 at 5% annual interest for 10 years.
# How much would I have?

# money = 5000
# for i in range(10):
#     money *= 1.05
# print(round(money, 2))

# e.g. 8 other versions of the for loop

# for i in range(5): # drop the start, it starts at 0
#     print(i)

# for i in range(0, 20, 2): # add 3rd value, it counts by that
#     print(i)

# for i in range(20, 0, -1):
#     print(i)

name = "Vincent Massey"
for letter in name:      #letter becomes each character in name, one at a time
    if letter not in "aeiouAEIOU":
        print(letter, end="")