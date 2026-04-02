from collections import Counter
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for row in grid:
    now = row[0]
    count = 0
    for e in row:
        if e == now:
            count += 1
        else:
            now = e
            count = 1
        if m == count:
            answer += 1
            break

for i in range(n):
    col = []
    for row in grid:
        col.append(row[i])
    now = col[0]
    count = 0
    for e in col:
        if e == now:
            count += 1
        else:
            now = e
            count = 1
        if m == count:
            answer += 1
            break

print(answer)