import math
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
memo = {1:1,2:1,3:2}

def fibo(n):
    if n in memo:
        return memo[n]
    else:
        if n%2 == 1:
            memo[n] = ((fibo(n//2)**2) + (fibo(n//2+1)**2)) % 1000000007
        else:
            memo[n] = (fibo(n+1) - fibo(n-1)) % 1000000007
    return memo[n] % 1000000007

print(fibo(math.gcd(n, m)))