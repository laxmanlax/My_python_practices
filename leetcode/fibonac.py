"""
1 1 2 3 5 7 ........

recursive solution
"""
def fib(n):
    if n==1 or n==2:
        return = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

"""
Memoized Solution
"""
def feb(n, memo):
    if memo[n]!=0:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n]= result
    return result 

"""
Bottom-Up Approach
"""
def fib_bottom_up(n):
    if n == 1 or n ==2:
        return 1
    bottom_up = [0 for i in range(len(n)+1)]

    bottom_up[1]=1
    bottom_up[2]=1

    for i in range(3, len(n)):
        bottom_up[i]=bottom_up[i-1]+ bottom_up[i-2]
    return bottom_up[n]




