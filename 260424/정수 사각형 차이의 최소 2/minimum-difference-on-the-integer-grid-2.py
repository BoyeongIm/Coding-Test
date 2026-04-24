n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
1. 경로마다 (min, max) 다름 → DP 터짐
2. 그러면 “좋은 경로 찾기” 말고
3. “이 조건을 만족하는 경로가 있나?”로 바꿔보자
-> 이분탐색 / 투포인터 + BFS/DFS
"""
from collections import deque
vals = sorted(set(num for row in grid for num in row))
def cango(L, R):
    if not (L <= grid[0][0] <= R):
        return False
    visited = [[False]*n for _ in range(n)]
    q = deque([(0,0)])
    visited[0][0] = True
    dxs, dys = [0,1], [1,0]
    while q:
        x, y = q.popleft()
        if x==n-1 and y==n-1:
            return True
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and L<=grid[nx][ny]<=R:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return False
ans = 199392992190
l = 0
for r in range(len(vals)):
    while l<=r:
        if cango(vals[l], vals[r]):
            ans = min(ans, vals[r]-vals[l])
            l += 1
        else:
            break
print(ans)