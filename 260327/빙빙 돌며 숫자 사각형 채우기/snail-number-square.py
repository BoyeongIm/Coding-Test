n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
def in_range(x,y):
    return 0<=x<n and 0<=y<m

dxs = [0,1,0,-1] # 시계방향
dys = [1,0,-1,0] 
'''
가로로 움직이는 것 == 열번호를 조정하는 것!!!
세로로 움직이는 것 == 행번호를 조정하는 것!!!
'''

x, y = 0, 0
dir = 0
arr[x][y] = 1

for i in range(2, n*m+1): # 총 돌아야 하는 횟수이자 채워넣야 하는 숫자로 for문 돌자
    nx, ny = x+dxs[dir], y+dys[dir]
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir = (dir+1) % 4
    x, y = x+dxs[dir], y+dys[dir]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()