n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [0,1,-1,0]
dys = [1,0,0,-1]

answer = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for x in range(n):
    for y in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                count += 1
        if count >= 3:
            answer += 1
print(answer)