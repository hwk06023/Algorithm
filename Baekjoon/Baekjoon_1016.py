a, b = map(int, input().split())

nlen = b - a + 1

sieve = [False] * nlen
i = 2

while True:
    k = i**2
    
    if k <= b:
        sNum = a // k
        if a % k != 0: sNum += 1

        while sNum * k <= b:
            if not sieve[sNum * k - a]:
                sieve[sNum * k  - a] = True
                nlen -= 1
            sNum += 1
        i += 1

    else:
        break

print(nlen)