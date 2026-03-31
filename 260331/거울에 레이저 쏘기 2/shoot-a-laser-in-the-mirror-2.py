n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 동(0), 남(1), 서(2), 북(3)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 슬래시: 북<->동, 남<->서
slash_reflect = [3,2,1.0]

# 백슬래시: 남<->동, 북<->서
backslash_reflect = [1,0,3,2]

side = (k-1) // n
offset = (k-1) % n

if side == 0: #남
    cx, cy = 0, offset
    dnum = 1 
elif side == 1: #서
    cx, cy = offset, n-1
    dnum = 2
elif side == 2: #북
    cx, cy = n-1, n-1-offset
    dnum = 3
else: #동
    cx, cy = n-1-offset, 0
    dnum = 0

nx, ny = cx, cy
answer = 0

while in_range(nx,ny):
    if grid[nx][ny] == "/":
        dnum = slash_reflect[dnum]
    else:
        dnum = backslash_reflect[dnum]
    
    nx, ny = nx+dxs[dnum], ny+dys[dnum]
    answer += 1

print(answer)