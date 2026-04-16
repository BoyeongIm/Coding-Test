n = int(input())
r1, c1, r2, c2 = map(int, input().split())
from collections import deque
# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs():
    visited = [[False]*n for _ in range(n)]
    dxs, dys = [-2,-2,-1,1,2,2,1,-1], [-1,1,2,2,1,-1,-2,-2]
    q = deque([(r1-1, c1-1, 0)])
    visited[r1-1][c1-1] = True

    while q:
        x,y,num = q.popleft()
        if x==r2-1 and y==c2-1:
            return num
            
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny, num+1))
                visited[nx][ny] = True

    return -1
print(bfs())