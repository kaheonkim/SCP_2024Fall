import math

def f1(x):
    return x

def f2(a,b):
    c = a + b
    return c

def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def triangle(a,b,c):
    s = (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return A

def factorial_recur(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*factorial_recur(n-1)
    
def T(n):
    if n == 1:
        return 2
    elif n >1:
        return 3+T(math.ceil(n/2))
    
def sum1(n):
    s = 0
    for i in range(1,n+1):
        s += i**3
    return s

def sum2(n):
    return (n*(n+1))**2//4

def saving(D, m = 100, r = 0.02):
    s = 0
    for i in range(m):
        s += D*(1+r)**i
    return s