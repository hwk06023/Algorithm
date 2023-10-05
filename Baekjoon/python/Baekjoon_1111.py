n = int(input())
li = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if li[0] == li[1]:
        print(li[0])
    else:
        print("A")
else:
    if li[0] == li[1]:
        a = 0
        b = li[0]
    else:
        a = (li[2] - li[1]) // (li[1] - li[0])
        b = li[1] - li[0] * a
    for i in range(1, n):
        if li[i] != li[i - 1] * a + b:
            print("B")
            break
    else:
        print(li[-1] * a + b)