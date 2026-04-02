from collections import Counter
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for row in grid:
    row_count = Counter(row)
    if m in row_count.values():
        answer += 1

for i in range(n):
    col = []
    for row in grid:
        col.append(row[i])
    col_count = Counter(col)
    if m in col_count.values():
        answer += 1
print(answer)