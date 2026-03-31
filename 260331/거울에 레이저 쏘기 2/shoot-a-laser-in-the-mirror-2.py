n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 북, 남, 서, 동 for "/"
dxs1 = [-1,1,0,0]
dys1 = [0,0,-1,1]

# 남, 북, 서, 동 for "\"
dxs2 = [1,-1,0,0]
dys2 = [0,0,-1,1]

side = (k-1) // n
offset = (k-1) % n

if side == 0:
    cx, cy = 0, offset
    dnum = 1 if grid[cx][cy]=="/" else 0
elif side == 1:
    cx, cy = offset, n-1
    dnum = 2
elif side == 2:
    cx, cy = n-1, n-1-offset
    dnum = 0 if grid[cx][cy]=="/" else 1
else:
    cx, cy = n-1-offset, 0
    dnum = 3

nx, ny = cx, cy
answer = 0

while in_range(nx,ny):
    if grid[nx][ny] == "/":
        dnum = 3-dnum
        nx, ny = nx+dxs1[dnum], ny+dys1[dnum]
    else:
        dnum = 3-dnum
        nx, ny = nx+dxs2[dnum], ny+dys2[dnum]
    answer += 1

print(answer)