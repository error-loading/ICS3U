# You won $1,000,000 in the lottery, and you want to take out enough each year to live on. Ignoring any tax concerns, you invest the money at 9% annual interest. At the beginning of each year you take out your money. The amount of money you take out is $50,000 in the first year, but increases by 12% each year. Write a program to figure out how many years the money will last, and how much money you would have in the last year.
# Date: Feb 23, 2023

num = 1000000
takeOut = 50000
invest = 1.09
increase = 1.12
year = 0

while num * invest - takeOut * increase > 0:
    print(f"Num: {num}, Takeout: {takeOut}")
    num *= invest
    takeOut *= increase
    num -= takeOut
    year += 1

print(year)