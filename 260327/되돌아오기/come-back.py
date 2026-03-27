n = int(input())
moves = [tuple(input().split()) for _ in range(n)]

dir_dict = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
sx, sy = 0,0
time = 0
cx, cy = 0,0
flag=False

for (d, dist) in moves:
    dist = int(dist)
    dx, dy = dir_dict[d]
    for i in range(dist):
        cx,cy = cx+dx, cy+dy
        time += 1
        if (cx,cy) == (sx, sy):
            flag = True
            break
        # 찾았다는 flag 변수 만들어서 관리하기!!
    if flag:
        break

print(time if flag else -1)