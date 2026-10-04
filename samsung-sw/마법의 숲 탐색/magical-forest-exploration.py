'''
숲의 동,서,남은 벽으로 막혀있음. 북쪽을 통해서 정령들이 들어옴.
K명의 정령이 골렘을 타고 숲을 탐색
- 각 골렘: 십자 모양의 구조, 중앙 포함 5칸
- 중앙 제외 4칸 중 한 칸은 골렘의 출구: 탑승은 어디서든 할 수 있지만 내릴 때는 출구를 통해서만
- i번째로 숲을 탐색하는 골렘: 중앙이 c_i열이 되도록 하는 위치에서 내려오기 시작
    - 출구: d_i(0~3, 순서대로 북,동,남,서)

골렘은 숲을 탐색하기 위해 다음과 같은 과정을 "더 이상 움직이지 못할 때까지 반복"
1. 남쪽으로 한칸 내려감 (동,서,남 방향에 대해서 아래가 모두 비어있을 때만)
2. 1이 불가능하면 서쪽 방향으로 회전
    - 출구가 반시계방향으로 이동
3. 둘 다 불가능하면, 동쪽 방향으로 회전
    - 출구가 시계방향으로 이동
4. 가장 남쪽에 도달해 더이상 이동 불가 -> 정령은 골렘 내에서 상하좌우 인접 칸으로 이동 가능
    - 단, 현재 골렘의 출구가 다른 골렘과 인접하고 있다면, 그 출구를 통해 다른 골렘으로 이동 가능
    - 정령은 갈 수 있는 모든 칸 중 가장 남쪽으로 이동하고 종료
    - 이때가 정령의 최종 위치

- 만약 골렘이 최대한 남쪽으로 이동했지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면, 지금 현재 골렘 포함 
  숲에 위치한 모든 골렘들은 숲을 빠져 나간 뒤, 다음 골렘부터 새롭게 시작 (이때의 최종 위치는 답 포함 안함) 

골렘들이 숲에 진입함에 따라 각 정령들이 최종적으로 위치한 행의 총합 구하기 (텅 비게 되어도 총합은 누적)
'''
from collections import deque
R, C, K = map(int, input().split())
golem_info = [tuple(map(int, input().split())) for _ in range(K)]   # 각 골렘 출발 열, 출구 방향
for i, (c, d) in enumerate(golem_info):
    golem_info[i] = (c-1, d)
'''
주의할 점: 계산 편의를 위해 0~n-1로 관리하니, 답을 구할 때는 현재 행 번호에 1을 더해서 반영하기
'''

forest = [[0]*C for _ in range(R+3)]
exit_grid = [[False]*C for _ in range(R+3)]
exit_dirs = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}  # 중앙 기준 북,동,남,서
dxs, dys = [-1,0,1,0],[0,1,0,-1]


def fillin(i, cx, cy, d):
    if forest[cx][cy] == 0:
        forest[cx][cy] = i+1
        for dx, dy in zip(dxs, dys):
            forest[cx+dx][cy+dy] = i+1
        ex, ey = cx+exit_dirs[d][0], cy+exit_dirs[d][1]
        exit_grid[ex][ey] = True

def to_south(cx, cy):
    bx, by= cx+1, cy
    return cx+2 < R+3 and forest[bx+1][by] == 0 and forest[cx+1][cy-1] == 0 and forest[cx+1][cy+1] == 0

def to_west(cx, cy):
    wx, wy = cx, cy-1
    return wy-1 >= 0 and cx+2 < R+3 and forest[wx][wy-1] == 0 and forest[cx-1][cy-1] == 0 and forest[cx+1][cy-1] == 0 \
    and forest[cx+1][cy-2] == 0 and forest[cx+2][cy-1] == 0

def to_east(cx, cy):
    ex, ey = cx, cy+1
    return ey+1 < C and cx+2 < R+3 and forest[ex][ey+1] == 0 and forest[cx-1][cy+1] == 0 and forest[cx+1][cy+1] == 0 \
    and forest[cx+2][cy+1] == 0 and forest[cx+1][cy+2] == 0

def move_spirit(sx, sy):
    gi = forest[sx][sy]
    q = deque([(sx, sy, gi)])
    visited = set()
    visited.add((sx, sy))
    max_row = sx
    while q:
        cx, cy, cgi = q.popleft()
        max_row = max(cx, max_row)
        if cx == R+2:
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<R+3 and 0<=ny<C and (nx, ny) not in visited:
                if exit_grid[cx][cy] and forest[nx][ny] != 0:
                    q.append((nx, ny, forest[nx][ny]))
                    visited.add((nx, ny))
                elif forest[nx][ny] == cgi:
                    q.append((nx, ny, cgi))
                    visited.add((nx, ny))
    return max_row

def out_range(cx, cy):
    return cx < 4

answer = 0
for i, (c, d) in enumerate(golem_info):
    cx, cy = 1, c

    while True:
        if to_south(cx, cy):
            cx += 1
        elif to_west(cx, cy):
            cx += 1
            cy -= 1
            d -= 1
            d = d%4
        elif to_east(cx, cy):
            cx += 1
            cy += 1
            d += 1
            d = d%4
        else:
            break
        
    if out_range(cx, cy):
        forest = [[0]*C for _ in range(R+3)]
        exit_grid = [[False]*C for _ in range(R+3)]
        continue

    fillin(i, cx, cy, d)
    fcx = move_spirit(cx, cy)
    answer += (fcx-2)

print(answer)