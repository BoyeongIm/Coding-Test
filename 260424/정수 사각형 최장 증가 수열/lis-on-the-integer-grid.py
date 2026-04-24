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
    # 초기화
    dp[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            # 조건을 만족하면, 현재 x,y의 dp값을 갱신해줌!!!
            ## 지금 현재 dp에 저장되어 있는 값이랑, 새롭게 탐색하는 nx,ny로 갔을 때의 결과와 비교
            dp[x][y] = max(dp[x][y], 1+dfs(nx, ny))
    return dp[x][y]

ans = -1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))

print(ans)