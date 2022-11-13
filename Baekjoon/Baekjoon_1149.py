num = int(input())

RGB_li = []

min_R = [0, 0, 0, 0]
min_G = [0, 0, 0, 0]
min_B = [0, 0, 0, 0]

min_RGB_Layer = [0, 0, 0]

for i in range(num):
    temp = list(map(int, input().split()))
    RGB_li.append(temp)

for i in range(2, num, 2):
    # i-2 ~ i까지 연산 가능한 경우를 모두 저장
    min_R = [RGB_li[i-2][2] + RGB_li[i-1][1] + RGB_li[i][0],
             RGB_li[i-2][1] + RGB_li[i-1][2] + RGB_li[i][0],
             RGB_li[i-2][0] + RGB_li[i-1][1] + RGB_li[i][0], 
             RGB_li[i-2][0] + RGB_li[i-1][2] + RGB_li[i][0]]
    
    min_G = [RGB_li[i-2][2] + RGB_li[i-1][0] + RGB_li[i][1],
             RGB_li[i-2][0] + RGB_li[i-1][2] + RGB_li[i][1],
             RGB_li[i-2][1] + RGB_li[i-1][0] + RGB_li[i][1], 
             RGB_li[i-2][1] + RGB_li[i-1][2] + RGB_li[i][1]]

    min_B = [RGB_li[i-2][0] + RGB_li[i-1][1] + RGB_li[i][2],
             RGB_li[i-2][1] + RGB_li[i-1][0] + RGB_li[i][2],
             RGB_li[i-2][2] + RGB_li[i-1][0] + RGB_li[i][2], 
             RGB_li[i-2][2] + RGB_li[i-1][1] + RGB_li[i][2]]

    # 위에 저장한 리스트 토대로 min 값 구함
    min_RGB_Layer[0] = min(min_R)
    min_RGB_Layer[1] = min(min_G)
    min_RGB_Layer[2] = min(min_B)

    print(min_RGB_Layer)

    # 위에 구한 min값을 토대로 next step [i-2]layer의 각 R G B 로 저장
    RGB_li[i] = min_RGB_Layer

# 마지막 RGB_li에 도달한 값들 R G B 중 최솟값이 답
print(min(RGB_li[num-1]))


'''
    [i-2], [i-1], [i] 각 층의 R G B 합해서 나올 수 있는 값
    
    그 중, 최소를 i가 R인 경우 G인 경우 B인 경우를 나누어 저장

    또 이 나누어 저장한 값을 하나의 층으로써 구성하여

    ex) R 
        [3 2 1, 2 3 1, 1 3 1, 1 2 1]
    ->  [[i-2][2] + [i-1][1] + [i][0], .. , [i-2][0] + [i-1][1] + [i][0]]
    ->  min(list)
    ->  R

    G -> .. -> G, B -> .. -> B

        [R, G, B] -> [1, 2 ,3] -> [[i-2][0], [i-2][1], [i-2][2]]

    이를 [i] -> [i-2] 층의 R G B로써 활용하면 풀릴 듯!
'''