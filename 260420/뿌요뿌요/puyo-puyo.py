n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False]*n for _ in range(n)]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y):
    cnt = 1
    dxs, dys = [1,0,0,-1], [0,1,-1,0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
            visited[nx][ny] = True
            cnt += dfs(nx, ny)
    return cnt

maxsize = -1
exploded = 0
for i in range(n):
    for j in range(n):
        visited[i][j] = True
        size = dfs(i,j)
        if size >= 4:
            exploded += 1
        maxsize = max(size, maxsize)

print(exploded, maxsize)