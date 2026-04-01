n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
x, y = n//2, n//2
dir_num = 0
walk_stage = 1 # 그 방향으로 몇번 이동해야 하는지
move_count = 0 # 지금 방향으로 이동한 칸 수 (walk_stage만큼이 되어야 함)
turn_count = 0 # 매 walk_stage마다 두번씩
grid_count = 1
grid[x][y] = 1

# 반시계: 동,북,서,남
dxs=[0,-1,0,1]
dys=[1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

while grid_count < n**2:
    if move_count == walk_stage:
        dir_num = (dir_num+1) % 4
        turn_count += 1
        move_count = 0
        if turn_count == 2:
            walk_stage += 1
            turn_count = 0
    else:
        x, y = x+dxs[dir_num], y+dys[dir_num]
        # if in_range(x,y) and grid[x][y] == 0:
        grid_count += 1
        grid[x][y] = grid_count
        move_count += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()