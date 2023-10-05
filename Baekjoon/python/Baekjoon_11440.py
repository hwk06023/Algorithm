n = int(input())

li = {0:0, 1:1, 2:1}
def fibo(n):
    global li
    if n % 2 == 0:
        k=n
        n //= 2
        if k not in li:
            li[k] = (fibo(n)**2 + 2*fibo(n)*fibo(n-1)) % 1000000007
        return li[k]
    else:
        k=n
        n += 1
        n //= 2
        if k not in li:
            li[k] = (fibo(n)**2 + fibo(n-1)**2) % 1000000007
        return li[k]
fibo(n+1)
fibo(n)

flag = li[n+1]**2 - li[n]**2
if n % 2 == 0:
    flag -= 1
else:
    flag += 1
    
print(flag % 1000000007)