import sys

input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
remove = int(input())

def remove_node(tree, remove):
    tree[remove] = -2
    for i in range(n):
        if tree[i] == remove:
            remove_node(tree, i)
    return tree

def count_leaf(tree):
    cnt = 0
    for i in range(n):
        if (tree[i] != -2) and (i not in tree):
            cnt += 1
    return cnt

remove_node(tree, remove)
print(count_leaf(tree))
