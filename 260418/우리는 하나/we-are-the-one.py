from collections import deque
from itertools import combinations_with_replacement, combinations
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<n

dots = [(i, j) for i in range(n) for j in range(n)]
starts = list(combinations(dots, k))
dxs = [1,0,0,-1]
dys = [0,1,-1,0]
maxcities = -1

for comb in starts:
    cities = k
    visited = [[False]*n for _ in range(n)]
    q = deque([])

    for x, y in comb:
        q.append((x,y))
        visited[x][y]=True
    while q:
        x, y = q.popleft()
        height1 = grid[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                height2 = grid[nx][ny]
                if u <= abs(height1-height2) <= d:
                    cities += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    maxcities = max(cities, maxcities)
print(maxcities)