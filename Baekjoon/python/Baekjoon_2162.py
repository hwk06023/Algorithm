import sys

input = sys.stdin.readline
n = int(input())
line_li = []
for _ in range(n):
    line_li.append(list(map(int, input().split())))

def ccw(p1,p2,p3):
    if (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0] == 0):
        return 0
    elif (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0] > 0):
        return 1
    else:
        return -1

def cross(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    p1=[x1,y1]
    p2=[x2,y2]
    p3=[x3,y3]
    p4=[x4,y4]

    if ccw(p1,p2,p3) * ccw(p1,p2,p4) == 0 and ccw(p3,p4,p1) * ccw(p3,p4,p2) == 0:
        a_x = max(x1, x2)
        b_x = min(x1, x2)
        c_x = max(x3, x4)
        d_x = min(x3, x4)

        a_y = max(y1, y2)
        b_y = min(y1, y2)
        c_y = max(y3, y4)
        d_y = min(y3, y4)

        if (x1 == x2 and x1 == x3) or (x1 == x2 and x1 == x4) or (x1 == x3 and x1 == x4) or (x2 == x3 and x2 == x4):
            if a_y < d_y or c_y < b_y:
                return False
            else:
                return True
        elif a_x < d_x or c_x < b_x:
            return False
        else:
            return True

    elif (ccw(p1,p2,p3) * ccw(p1,p2,p4) <= 0) and (ccw(p3,p4,p1) * ccw(p3,p4,p2) <= 0) :
        return True
    else:  
        return False

linegroup_li = [[line_li[0]]]

for i in range(1, n):
    line = line_li[i]
    flag = False
    flag_num = 0
    j = 0
    while j < len(linegroup_li):
        for x in linegroup_li[j]:
            if cross(line, x):
                if flag:
                    linegroup_li[flag_num].extend(linegroup_li[j])
                    linegroup_li.pop(j)
                    break
                else:
                    linegroup_li[j].append(line)
                    flag_num = j
                    flag = True
                    j += 1
                    break
        else:
            j += 1
    if not flag:
        linegroup_li.append([line])

print(len(linegroup_li))
print(max([len(linegroup_li[i]) for i in range(len(linegroup_li))]))
