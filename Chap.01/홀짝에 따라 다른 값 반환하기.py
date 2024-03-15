def odd(n):
    return sum(i for i in range(1, n+1, 2))

def even(n):
    return sum(i**2 for i in range(2, n+1, 2))

def solution(n):
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)