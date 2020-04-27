def fib(N):
    if N == 0:
        return 0
    elif N <= 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
