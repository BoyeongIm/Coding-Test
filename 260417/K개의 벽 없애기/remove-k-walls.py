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
    # k값마다 방문 상태가 별개로 관리되어야 함. 
    visited = [[[False]*(k+1) for _ in range(n)] for _ in range(n)]
    dxs, dys = [1,0,0,-1],[0,1,-1,0]
    q = deque([(r1, c1, 0, k)])
    visited[r1][c1][k] = True

    while q:
        x,y,time,left = q.popleft()
        if x==r2 and y==c2:
            return time
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny][left]:
                if grid[nx][ny] == 1 and left > 0:
                    q.append((nx, ny, time+1, left-1))
                    visited[nx][ny][left-1] = True
                elif grid[nx][ny] == 0:
                    q.append((nx, ny, time+1, left))
                    visited[nx][ny][left] = True

    return -1

print(bfs(k))