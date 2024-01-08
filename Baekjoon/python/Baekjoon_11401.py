import sys

input = sys.stdin.readline

n, k = map(int, input().split())

factorial = {0:1, 1:1}

def factorial_dp(k):
    if k in factorial:
        return factorial[k]
    for i in range(2, k+1):        
        factorial[i] = factorial[i-1] * i
        if factorial[i] % 1000000007 != 0:
            factorial[i] %= 1000000007       
    return factorial[k]

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return (tmp**2 * n) % 1000000007
    else:
        return tmp**2 % 1000000007

print((factorial_dp(n) * square(factorial_dp(k) * factorial_dp(n-k), 1000000005) % 1000000007)) # 페르마 소정리
