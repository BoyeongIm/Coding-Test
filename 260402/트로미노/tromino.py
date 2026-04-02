n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_value = 0
## type 1: 일자 3개
for row in grid:
    for j in range(m-2):
        rowsum = sum(row[j:j+3])
        if max_value < rowsum:
            max_value = rowsum
for j in range(m):
    for i in range(n-2):
        colsum = grid[i][j]+grid[i+1][j]+grid[i+2][j]
        if max_value < colsum:
            max_value = colsum

## type 2: ㄴ자 3개
for i in range(n-1):
    for j in range(m-1):
        vals = []
        rows = grid[i:i+2]
        for r in rows:
            cols = r[j:j+2]
            for c in cols:
                vals.append(c)
        vals.sort(reverse=True)
        val_sum = sum(vals[:3])
        if max_value < val_sum:
            max_value = val_sum

print(max_value)