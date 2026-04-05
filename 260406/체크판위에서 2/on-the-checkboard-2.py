R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt = 0
std = grid[0][0]
for i in range(1, R-2):
    for j in range(1, C-2):
        if grid[i][j] != std:
            std = grid[i][j]
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if std != grid[k][l]:
                    cnt += 1
        std = grid[0][0]
if grid[0][0] == grid[R-1][C-1]:
    cnt = 0
print(cnt)