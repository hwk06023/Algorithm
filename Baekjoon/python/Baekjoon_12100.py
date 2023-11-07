n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
flag = 0
max_value = 0

class Move:
    def __init__(self, maps, n):
        self.maps = maps
        self.n = n

    def move_up(self):
        for j in range(self.n):
            for i in range(self.n):
                if self.maps[i][j] != 0:
                    for k in range(i+1, self.n):
                        if self.maps[k][j] != 0:
                            if self.maps[i][j] == self.maps[k][j]:
                                self.maps[i][j] *= 2
                                self.maps[k][j] = 0
                            break
        for j in range(self.n):
            for i in range(self.n):
                if self.maps[i][j] == 0:
                    for k in range(i+1, self.n):
                        if self.maps[k][j] != 0:
                            self.maps[i][j] = self.maps[k][j]
                            self.maps[k][j] = 0
                            break

    def move_down(self):
        for j in range(self.n):
            for i in range(self.n-1, -1, -1):
                if self.maps[i][j] != 0:
                    for k in range(i-1, -1, -1):
                        if self.maps[k][j] != 0:
                            if self.maps[i][j] == self.maps[k][j]:
                                self.maps[i][j] *= 2
                                self.maps[k][j] = 0
                            break
        for j in range(self.n):
            for i in range(self.n-1, -1, -1):
                if self.maps[i][j] == 0:
                    for k in range(i-1, -1, -1):
                        if self.maps[k][j] != 0:
                            self.maps[i][j] = self.maps[k][j]
                            self.maps[k][j] = 0
                            break

    def move_left(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.maps[i][j] != 0:
                    for k in range(j+1, self.n):
                        if self.maps[i][k] != 0:
                            if self.maps[i][j] == self.maps[i][k]:
                                self.maps[i][j] *= 2
                                self.maps[i][k] = 0
                            break
        for i in range(self.n):
            for j in range(self.n):
                if self.maps[i][j] == 0:
                    for k in range(j+1, self.n):
                        if self.maps[i][k] != 0:
                            self.maps[i][j] = self.maps[i][k]
                            self.maps[i][k] = 0
                            break

    def move_right(self):
        for i in range(self.n):
            for j in range(self.n-1, -1, -1):
                if self.maps[i][j] != 0:
                    for k in range(j-1, -1, -1):
                        if self.maps[i][k] != 0:
                            if self.maps[i][j] == self.maps[i][k]:
                                self.maps[i][j] *= 2
                                self.maps[i][k] = 0
                            break
        for i in range(self.n):
            for j in range(self.n-1, -1, -1):
                if self.maps[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if self.maps[i][k] != 0:
                            self.maps[i][j] = self.maps[i][k]
                            self.maps[i][k] = 0
                            break

def dfs(maps, n, cnt):
    global max_value
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if maps[i][j] > max_value:
                    max_value = maps[i][j]
        return
    for i in range(4):
        move = Move(maps, n)
        if i == 0:
            move.move_up()
        elif i == 1:
            move.move_down()
        elif i == 2:
            move.move_left()
        else:
            move.move_right()
        dfs(move.maps, n, cnt+1)

dfs(maps, n, 0)
print(max_value)
