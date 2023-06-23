x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1=[x1,y1]
p2=[x2,y2]
p3=[x3,y3]
p4=[x4,y4]

def ccw(p1,p2,p3):
    if (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0] == 0):
        return 0
    elif (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0] > 0):
        return 1
    else:
        return -1

if ccw(p1,p2,p3) * ccw(p1,p2,p4) == 0 and ccw(p3,p4,p1) * ccw(p3,p4,p2) == 0:
    a_x = max(x1, x2)
    b_x = min(x1, x2)
    c_x = max(x3, x4)
    d_x = min(x3, x4)

    a_y = max(y1, y2)
    b_y = min(y1, y2)
    c_y = max(y3, y4)
    d_y = min(y3, y4)

    if x1 == x2 and x1 == x3 and x1 == x4:
        if a_y < d_y or c_y < b_y:
            print(0)
        else:
            print(1)
    elif a_x < d_x or c_x < b_x:
        print(0)
    else:
        print(1)

elif (ccw(p1,p2,p3) * ccw(p1,p2,p4) <= 0) and (ccw(p3,p4,p1) * ccw(p3,p4,p2) <= 0) :
    print(1)
else:  
    print(0)