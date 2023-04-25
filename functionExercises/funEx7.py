def fact(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    
    return n * fact(n-1) 


def pascal(first, second):
    return fact(first) // (fact(second) * fact(first - second))

print(pascal(4, 3))