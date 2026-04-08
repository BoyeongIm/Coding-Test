N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
def in_range(x,y):
    return 0<=x<N and 0<=y<M
# 북쪽부터 시계방향
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]
cnt = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == "L":
            for i in range(8):
                nx, ny = x+dxs[i], y+dys[i]
                nx2, ny2 = nx+dxs[i], ny+dys[i]
                if in_range(nx, ny) and in_range(nx2, ny2):
                    if arr[nx][ny] == arr[nx2][ny2] == "E":
                        cnt += 1

print(cnt)