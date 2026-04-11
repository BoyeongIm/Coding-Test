import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_size = sys.maxsize
for i in range(n):
    max_x = -1
    max_y = -1
    min_x = sys.maxsize
    min_y = sys.maxsize
    for j in range(n):
        if i == j:
            continue
        min_x = min(x[j], min_x)
        max_x = max(x[j], max_x)
        min_y = min(y[j], min_y)
        max_y = max(y[j], max_y)
    size = (max_x - min_x) * (max_y - min_y)
    min_size = min(size, min_size)
print(min_size)
