# Gurjas Dhillon
# repititionEx2.py
# This program starts with 8.017 billion, and finds the number of years it takes to double the population when its increasing at the rate of 0.9%

# Given  that  the  current  world  population  is 8.017  billion and  increasing  at  the  rate  of 0.9% per  year, calculate the number of years it would take for the world population to double at the current rate

population = 8.017
curPopulation = 8.017
years = 0
rate = 1.009

while curPopulation < population * 2:
    years += 1
    curPopulation *= rate

print(f"It will take {years} years to double the population")