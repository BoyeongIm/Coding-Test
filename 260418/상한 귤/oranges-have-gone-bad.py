from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x,y):
    return 0<=x<n and 0<=y<n
dxs = [1,0,0,-1]
dys = [0,1,-1,0]
q = deque([])
timegrid = [[-2]*n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            q.append((x, y, 0))
            timegrid[x][y] = 0
            visited[x][y] = True 

while q:
    x, y, time = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            timegrid[nx][ny] = time+1
            q.append((nx, ny, time+1))
            visited[nx][ny] = True

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            timegrid[i][j] = -1
        print(timegrid[i][j], end=' ')
    print()