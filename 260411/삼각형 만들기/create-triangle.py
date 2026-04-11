n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def triangle(s1, s2, x1, y1, x2, y2):
    real_x = max(abs(s1-x1), abs(s1-x2))
    real_y = max(abs(s2-y1), abs(s2-y2))
    return real_x * real_y

max_size = 0
for i in range(n-2):
    x1, y1 = x[i], y[i]
    for j in range(i+1, n-1):
        x2, y2 = x[j], y[j]
        for k in range(j+1, n):
            x3, y3 = x[k], y[k]
            size = 0
            if (x1==x2 and y1==y3) or (x1==x3 and y1==y2):
                size = triangle(x1, y1, x2, y2, x3, y3)
            elif (x2==x3 and y2==y1) or (x2==x1 and y2==y3):
                size = triangle(x2, y2, x1, y1, x3, y3)
            elif (x3==x1 and y3==y2) or (x3==x2 and y3==y1):
                size = triangle(x3, y3, x1, y1, x2, y2)
            max_size = max(max_size, size)
print(max_size)