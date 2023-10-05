import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

tmp = 0

def merge_sort(li):
    if len(li) < 2:
        return li

    k = len(li) // 2

    left = merge_sort(li[:k])
    right = merge_sort(li[k:])

    merge_li = []
    l = 0
    h = 0
    global tmp
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merge_li.append(left[l])
            l += 1
        else:
            tmp += len(left) + h - len(merge_li)
            merge_li.append(right[h])
            h += 1
    merge_li += left[l:]
    merge_li += right[h:]
    return merge_li

merge_sort(li)

print(tmp)