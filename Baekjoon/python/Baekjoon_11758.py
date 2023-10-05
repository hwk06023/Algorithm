'''
li = []
for i in range(3):
    li.append(list(map(int, input().split())))

gradient_1 = (li[1][1] - li[0][1]) / (li[1][0] - li[0][0])
bias = li[1][1] - gradient_1*li[1][0]

if(li[2][1] == gradient_1*li[2][0] + bias):
    print(0)
elif(li[2][1] < gradient_1*li[2][0] + bias):
    print(-1)
else:
    print(1)

''' # ZeroDivision issue
li = []
for i in range(3):
    li.append(list(map(int, input().split())))

ccw = li[0][0]*li[1][1] + li[1][0]*li[2][1] + li[2][0]*li[0][1] - li[1][0]*li[0][1] - li[2][0]*li[1][1] - li[0][0]*li[2][1]

if (ccw == 0):
    print(0)
elif (ccw > 0):
    print(1)
else:
    print(-1)