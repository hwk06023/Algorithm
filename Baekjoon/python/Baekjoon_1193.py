x = int(input())
n = 1

while x > n:
    x -= n
    n += 1

if n % 2 == 0:
    print(str(x)+"/"+str(n-x+1))
else:
    print(str(n-x+1)+"/"+str(x))

