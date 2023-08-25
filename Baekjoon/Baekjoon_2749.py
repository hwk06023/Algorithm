n = int(input())
li = [0, 1]

if n >= 1500000:
    for i in range(2, 1500000):
        li.append((li[i-1] + li[i-2]) % 1000000)
    print(li[n%1500000])
else:
    for i in range(n-1):
        li.append(((li[0] % 1000000)+(li[1] % 1000000)) % 1000000)
        del li[0]
    print(li[1] % 1000000)
