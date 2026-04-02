n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
max_gold = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs1 = [1,0,-1,0]
dys1 = [0,1,0,-1]

dxs2 = [1,0,-1,0,2,0,-2,0,1,-1,1,-1]
dys2 = [0,1,0,-1,0,2,0,-2,-1,1,1,-1]

for x in range(n):
    for y in range(n):
        for k in range(3):
            cost = k**2 + (k+1)**2
            gold = grid[x][y]
            if k==1:
                for d in range(4):
                    nx,ny = x+dxs1[d], y+dys1[d]
                    if in_range(nx, ny) and grid[nx][ny] == 1:
                        gold += 1
            elif k==2:
                for d in range(len(dxs2)):
                    nx, ny = x+dxs2[d], y+dys2[d]
                    if in_range(nx, ny) and grid[nx][ny] == 1:
                        gold += 1
            if gold * m - cost >= 0 and max_gold < gold:
                max_gold = gold

print(max_gold)