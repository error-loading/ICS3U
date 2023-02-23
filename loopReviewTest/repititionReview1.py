# Write a program that gets numbers from the user until they enter zero then tells the user the average of all the numbers, the largest number entered, the smallest number entered and the number of negative numbers.
# Date: Feb 23

num = int(input("Enter a number: "))

ttl = 0
numN = 0
largest = float('-inf')
small = float('inf')
numNeg = 0

while num != 0:
    ttl += num
    numN +=1

    largest = max(largest, num)
    small = min(small, num)

    if num < 0:
        numNeg +=1
    
    num = int(input("Enter a number: "))

avg = ttl / numN

print(f"Average: {round(avg, 1)}")
print(f"Largest: {largest}")
print(f"Smallest: {small}")
print(f"Number of negatives: {numNeg}")
