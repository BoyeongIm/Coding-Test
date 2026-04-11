n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

min_dist = 9999999
for i in range(n-1):
    for j in range(i+1, n):
        min_dist = min(min_dist, distance(x[i], y[i], x[j], y[j]))

print(min_dist)