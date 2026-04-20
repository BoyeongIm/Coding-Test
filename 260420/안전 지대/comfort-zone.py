n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxnum_area = -1
maxk = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def dfs(x, y, k):
    dxs, dys = [0,1,-1,0], [1,0,0,-1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > k:
            visited[nx][ny] = True
            dfs(nx, ny, k)

for k in range(1, max(max(grid))+1):
    visited = [[False]*m for _ in range(n)]
    num_area = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, k)
                num_area += 1
    if maxnum_area < num_area:
        maxk = k
        maxnum_area = num_area

print(maxk, maxnum_area)