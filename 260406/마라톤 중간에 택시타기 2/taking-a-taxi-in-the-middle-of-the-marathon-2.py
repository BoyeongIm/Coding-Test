import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def manhattan(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

mindist = sys.maxsize
# Please write your code here.
for i in range(1, n-1):
    dist = 0
    for j in range(n-1):
        if j+1 == i:
            dist += manhattan(x[j], x[j+2], y[j], y[j+2])
        elif j==i:
            continue
        else:
            dist += manhattan(x[j], x[j+1], y[j], y[j+1])
    mindist = min(dist, mindist)
print(mindist)