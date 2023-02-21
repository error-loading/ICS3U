for i in range(10, 100):
    ttl = 0
    num = i
    while True:
        per = 1
        for j in str(num):
            per *= int(j)
        ttl +=1
        if per < 10:
            break
        num = per
        
    if ttl > 3:
        print(i, ttl)
        break