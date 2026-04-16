from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<m

visited = [[False]*m for _ in range(n)]
dxs, dys = [-1,0,0,1], [0,1,-1,0]
q = deque([(0,0,0)])
visited[0][0] = True

while q:
    x,y,dist = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx,ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and a[nx][ny] == 1:
            q.append((nx, ny, dist+1))
            visited[nx][ny] = True
            
if dist > 0:
    print(dist)
else:
    print(-1)