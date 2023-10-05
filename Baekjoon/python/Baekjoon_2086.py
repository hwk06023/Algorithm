a, b = map(int, input().split())

li = {0:0, 1:1, 2:1}
def fibo(n):
    global li
    if n % 2 == 0:
        k=n
        n //= 2
        if k not in li:
            li[k] = (fibo(n)**2 + 2*fibo(n)*fibo(n-1)) % 1000000000
        return li[k]
    else:
        k=n
        n += 1
        n //= 2
        if k not in li:
            li[k] = (fibo(n)**2 + fibo(n-1)**2) % 1000000000
        return li[k]
if a == b:
    fibo(a)
    print(li[a] % 1000000000)
else:
    fibo(a+1)
    fibo(b+2)
    print((li[b+2] - li[a+1]) % 1000000000)