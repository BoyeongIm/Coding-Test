n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.
dxs, dys = [1,0,0,-1], [0,1,-1,0]
visited = [[False]*n for _ in range(n)]
ans = 0
def cango(x, y):
    return 0<=x<n and 0<=y<n and grid[x][y]==0

def dfs(x, y, idx):
    global ans
    if idx >= m:
        ans += 1
        return 
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if cango(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            if points[idx] != (nx, ny):
                dfs(nx, ny, idx)
            else:
                dfs(nx, ny, idx+1)
            visited[nx][ny] = False

start_x, start_y = points[0][0], points[0][1]
visited[start_x][start_y] = True
first_idx = 1
dfs(start_x, start_y, first_idx)
print(ans)