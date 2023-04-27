# Recursion is when a function calls itself.
# For it to work properly, you need two things:
# 1. Base Case: This is a situation where the function does not call itself.

# 2. Recursive call: The function must call itself in a way that approaches the base case.

def hello(n):
    print("hello", n)
    if n > 0:
        hello(n-1)
    print("Bye", n)

hello(5)