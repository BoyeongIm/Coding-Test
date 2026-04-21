n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
locs = []
dxs1, dys1 = [-2,-1,1,2], [0,0,0,0]
dxs2, dys2 = [-1,1,0,0], [0,0,1,-1]
dxs3, dys3 = [-1,-1,1,1], [1,-1,-1,1]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            locs.append((i, j))
bombs = [0] * len(locs)
maxsize = -1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(idx):
    global maxsize
    if idx == len(locs):
        check = [[False]*n for _ in range(n)]
        for idx, bombtype in enumerate(bombs):
            x, y = locs[idx]
            check[x][y] = True
            if bombtype == 1:
                for dx, dy in zip(dxs1, dys1):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        check[nx][ny] = True
            elif bombtype == 2:
                for dx, dy in zip(dxs2, dys2):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        check[nx][ny] = True
            elif bombtype == 3:
                for dx, dy in zip(dxs3, dys3):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        check[nx][ny] = True
        exploded = sum(sum(row) for row in check)
        maxsize = max(maxsize, exploded)
        return
    for i in range(1,4):
        bombs[idx] = i
        dfs(idx+1)
        bombs[idx] = 0

dfs(0)
print(maxsize)