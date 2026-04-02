n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
max_gold = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for x in range(n):
    for y in range(n):
        for k in range(2*n+1):
            cost = k**2 + (k+1)**2
            gold =0 
            for nx in range(n):
                for ny in range(n):
                    if abs(nx-x)+abs(ny-y) <= k:
                        if in_range(nx, ny) and grid[nx][ny] == 1:
                            gold += 1
            if gold * m - cost >= 0 and max_gold < gold:
                max_gold = gold

print(max_gold)