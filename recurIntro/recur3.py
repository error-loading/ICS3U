# def fib(n):
#     if n == 1 or n == 2:
#         return 1
    
#     return fib(n-1) + fib(n-2)

# print(fib(6))

memo = {1 : 1, 2 : 1}

def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

print(fib(6))