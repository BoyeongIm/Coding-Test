n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[False]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

for x, y in points:
    cx, cy = x-1, y-1
    grid[cx][cy] = True
    num = 0
    for dx, dy in zip(dxs, dys):
        nx,ny = cx+dx, cy+dy
        if in_range(nx,ny) and grid[nx][ny]:
            num += 1
    if num == 3:
        print(1)
    else:
        print(0)