n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_count = -1
for sx in range(n):
    for sy in range(m):
        for ex in range(sx, n):
            for ey in range(sy, m):
                flag = True
                for x in range(sx, ex+1):
                    for y in range(sy, ey+1):
                        if grid[x][y] <= 0:
                            flag = False
                if flag:
                    size = (ex-sx+1) * (ey-sy+1)
                    if size > max_count:
                        max_count = size
print(max_count)