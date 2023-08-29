class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    
def pre_order(node):
    print(node.value, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right !=  '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.value, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.value, end='')

n = int(input())
tree = {}

for i in range(n):
    value, left, right = input().split()
    tree[value] = Node(value, left, right)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])