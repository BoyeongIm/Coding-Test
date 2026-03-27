n = int(input())
moves = [tuple(input().split()) for _ in range(n)]

dir_dict = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
sx, sy = 0,0
time = 0
cx, cy = 0,0

for (d,n) in moves:
    n = int(n)
    dx, dy = dir_dict[d]
    for i in range(n):
        cx,cy = cx+dx, cy+dy
        time += 1
        if cx==sx and cy==sy:
            break
    if cx==sx and cy==sy:
        break

if cx==sx and cy==sy:
    print(time)
else:
    print(-1)