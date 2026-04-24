n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [0,1,-1,0],[1,0,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

dp = [[0]*n for _ in range(n)]
def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[nx][ny] = max(dp[x][y], 1+dfs(nx, ny))
    return dp[x][y]
ans = -1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))

print(ans)