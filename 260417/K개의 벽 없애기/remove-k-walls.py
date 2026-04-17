n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
from collections import deque
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(k):
    visited = [[False]*n for _ in range(n)]
    dxs, dys = [1,0,0,-1],[0,1,-1,0]
    q = deque([(r1, c1, 0, k)])
    visited[r1][c1] = True

    while q:
        x,y,time,k = q.popleft()
        if x==r2 and y==c2 and k==0:
            return time
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if grid[nx][ny] == 1 and k > 0:
                    k -= 1
                elif grid[nx][ny] == 1 and k <= 0:
                    continue
                q.append((nx, ny, time+1, k))
                visited[nx][ny] = True
    
    return -1

print(bfs(k))