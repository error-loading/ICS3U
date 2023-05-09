'''
Gurjas Dhillon
funcAssign1.py
function that takes in a number and outputs the number of factors
'''

def numFactors(n):
    ttl = 0

    for i in range(1, n+1):
        if not n % i:
            ttl += 1
    
    return ttl

print(numFactors(16))