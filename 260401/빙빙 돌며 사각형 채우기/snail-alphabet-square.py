n, m = map(int, input().split())

# Please write your code here.
grid = [['.']*m for _ in range(n)]

# 시계방향: 동남서북
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

x, y = 0, 0
dir_num = 0
grid[x][y] = "A"
char_count = 1

for i in range(1, n*m):
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or grid[nx][ny] != ".":
        dir_num = (dir_num+1) % 4

    x, y = x+dxs[dir_num], y+dys[dir_num]
    grid[x][y] = chr(ord("A")+(char_count%26))
    char_count += 1

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()