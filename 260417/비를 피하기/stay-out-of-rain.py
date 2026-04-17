n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
ans = [[0]*n for _ in range(n)]
dxs,dys = [0,1,-1,0], [1,0,0,-1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for i in range(n):
    for j in range(n):
        q = deque([])
        visited = [[False]*n for _ in range(n)]
        if grid[i][j] == 2:
            q.append((i,j,0))
            visited[i][j] = True

            while q:
                x,y,dist = q.popleft()
                if grid[x][y] == 3:
                    ans[i][j] = dist
                    break
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny) and grid[nx][ny]!=1 and not visited[nx][ny]:
                        q.append((nx, ny, dist+1))
                        visited[nx][ny] = True
                if ans[i][j] == 0:
                    ans[i][j] = -1

for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()