N, T = map(int, input().split())
orders = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
## 방향: 북, 동, 남, 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

x, y = N//2, N//2
dir_num = 0
answer = board[x][y]

def in_range(x, y):
    return 0<=x<N and 0<=y<N

for o in orders:
    if o == "F":
        nx, ny = x+dxs[dir_num], y+dys[dir_num]
        if in_range(nx, ny):
            answer += board[nx][ny]
            x, y = nx, ny
    elif o == "R":
        dir_num = (dir_num+1)%4
    else:
        dir_num = (dir_num-1)%4

print(answer)