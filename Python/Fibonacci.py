#  Fibonacci series up to n
def fib(n):
    a=0
    b=1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
