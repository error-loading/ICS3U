def per(n, time):
    n = str(n)
    if len(n) == 1:
        print(time)
        return
    
    prod = 1
    for char in n:
        prod *= int(char)
    per(prod, time + 1)

per(35, 0)

