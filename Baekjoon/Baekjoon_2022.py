x, y, c = map(float, input().split())

start = 0
end = min(x, y)

def get_c(x, y, f) :
    m = (x**2 - f**2)**0.5
    n = (y**2 - f**2)**0.5
    c = m*n / (m+n)
    return c

flag = 0
while (end-start) > 0.0000001:
    f = (start+end)/2
    flag = f   
    if get_c(x, y, f) >= c:
        start = f
    else:
        end = f

print(round(flag, 4))