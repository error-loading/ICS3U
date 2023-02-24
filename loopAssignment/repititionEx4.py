# Gurjas Dhillon
# repititionEx4.py
# This program looks at all the 2 digit numbers and calculates the persistance of each, if its persistance is greater then 3, then we break out the loop and output the number


# loops through all the 2 digits numbers
for i in range(10, 100):
    per = 0     # this holds the persitance level of the number so far
    num = i
    while True:
        ttl = 1    # loops through the current number and multiplies the digits
        # could hv also done integer division and modulus but that is not scalable for bigger numbers
        for j in str(num):
            ttl *= int(j)
        per +=1

        # if the multiplication of the digits is less than 10, break out the loop
        if ttl < 10:
            break
        num = ttl
        
    if per > 3:
        print(f"{i} has a persistance of {per}.")
        break