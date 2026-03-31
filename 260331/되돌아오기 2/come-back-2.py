commands = input()

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

sx, sy = 0,0
dnum = 3
time = 0
nx, ny = 0,0
flag = False

for c in commands:
    if c == "F":
        nx, ny = nx+dxs[dnum], ny+dys[dnum]
        time += 1
    elif c == "L":
        dnum = (dnum-1) % 4
        time += 1
    elif c == "R":
        dnum = (dnum+1) % 4
        time += 1
    
    if (nx, ny) == (sx, sy):
        flag = True
        break

if flag:
    print(time)
else:
    print(-1)