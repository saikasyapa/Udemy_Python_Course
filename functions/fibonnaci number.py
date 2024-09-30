def fibonacci(n: int) -> int:
    """ Return the `n` th Fibonacci number, for positive `n` ."""
    a = 0
    b = 1
    if n<0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n ==1:
        return b
    else:
        for i in range(2,n + 1):
            c = a + b
            a = b
            b = c
            print(f"fibonacci series for {i} is {c}")
        return c

print(fibonacci(36))



