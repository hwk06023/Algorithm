class Tree:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n + 1)]
        self.parent = [0 for _ in range(n + 1)]

    def add(self, a, b):
        self.tree[a].append(b)
        self.tree[b].append(a)


def bfs(tree, start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        for i in tree.tree[node]:
            if tree.parent[i] == 0:
                tree.parent[i] = node
                queue.append(i)

n = int(input())
tree = Tree(n)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree.add(a, b)

bfs(tree, 1)

for i in range(2, n + 1):
    print(tree.parent[i])


                    
