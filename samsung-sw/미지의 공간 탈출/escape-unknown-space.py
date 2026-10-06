'''
N*N 미지의 공간. 그 사이 어딘가에 한 변의 길이가 M인 정육면체 형태의 시간의 벽
타임머신의 스캔 기능
    1. 미지의 공간의 평면도 (위에서 내려다본 전체 맵)
    2. 시간의 벽의 단면도 (윗면과, 동서남북 네 면의 단면도)
    - 모두 빈 공간(0)과 장애물(1)로 구성됨.
    - 타임머신은 빈 공간만 이동할 수 있으며, 장애물로는 이동 불가

- 타임머신은 시간의 벽 윗면 어딘가에 위치
- (시간의 벽 윗면) 타임머신의 위치 2, (미지의 공간 평면도) 시간의 벽 위치 3, 탈출구 4
    - 탈출구는 시간의 벽 외부에 있는 미지의 공간의 바닥에 위치  
- 시간의 벽과 맞닿은 미지의 공간의 바닥은 기본적으로 장애물로 둘러 쌓여있음.
    - 단 한 칸만 빈 공간으로 뚫려 있음.
    - 시간의 벽-미지의 공간 바닥 이어지는 곳은 단 하나
    - 시간의 벽을 둘러싸는 애들 중에 유일하게 값이 0인 곳!!
** 시간 이상 현상 **
    - 총 F개의 시간 이상 현상 (미지의 공간 바닥)
    - 바닥 빈 공간 (r,c) 에서 시작해 매 v의 배수 턴마다 방향 d로 한 칸씩 확산
        - d = (동서남북) = (0,1,2,3)
    - 장애물과 탈출구가 없는 빈 공간으로만 확산됨 (더 이상 확산 불가능할 때까지)
    - 타임머신은 시간 이상 현상이 확산되는 곳으로 이동할 수 없음.

- 매 턴마다 상하좌우로 한칸씩 이동 가능
    - 장애물과 시간 이상 현상을 피해, 탈출구까지 도달해야 함
- 필요한 최소 시간 (턴 수) 출력, 탈출 불가능하면 -1
'''
from collections import deque, defaultdict
N, M, F = map(int, input().split())
# 동서남북
dirs = {0:(0,1), 1:(0,-1), 2:(1,0), 3:(-1,0)}
overall_map = [list(map(int, input().split())) for _ in range(N)]

tm, exitt = None, None
# 타임머신 초기 위치와 최종 탈출구 위치 찾기
for i in range(N):
    for j in range(N):
        if overall_map[i][j] == 4:
            exitt = (i,j)
        if overall_map[i][j] == 2:
            tm = (i,j)
    if tm and exitt:
        break

east = [list(map(int, input().split())) for _ in range(M)]
# 반시계 방향 90도
rotated_east = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        rotated_east[M-1-j][i]= east[i][j]
west = [list(map(int, input().split())) for _ in range(M)]
# 시계 방향 90도
rotated_west = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        rotated_west[j][M-1-i] = west[i][j]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
# 180도 반전 필요
rotated_north = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        rotated_north[M-1-i][M-1-j] = north[i][j]
top = [list(map(int, input().split())) for _ in range(M)]

# 시간 이상 현상 그리드 미리 계산
INF = float('inf')
abnormal = [[INF] * N for _ in range(N)]
for _ in range(F):
    r, c, d, v = map(int, input().split())
    sx, sy = r, c
    abnormal[sx][sy] = 0
    go_x, go_y = dirs[d]
    t = 1
    while 0<=sx+go_x<N and 0<=sy+go_y<N:
        nx, ny= sx+go_x, sy+go_y
        if overall_map[nx][ny] != 0:
            break
        abnormal[nx][ny] = min(abnormal[nx][ny], t*v)
        sx, sy = nx, ny
        t += 1

# 시간의 벽 펼치기
folded_walls = [[-1]*3*M for _ in range(3*M)]
folded_tx, folded_ty = None, None
for i in range(M, 2*M):
    for j in range(M, 2*M):
        folded_walls[i][j] = top[i-M][j-M]
        if folded_walls[i][j] == 2:
            folded_tx, folded_ty = i,j
for i in range(0, M):
    for j in range(M, 2*M):
        folded_walls[i][j] = rotated_north[i][j-M]
for i in range(2*M, 3*M):
    for j in range(M, 2*M):
        folded_walls[i][j] = south[i-2*M][j-M]
for i in range(M, 2*M):
    for j in range(M):
        folded_walls[i][j] = rotated_west[i-M][j]
for i in range(M, 2*M):
    for j in range(2*M, 3*M):
        folded_walls[i][j] = rotated_east[i-M][j-2*M]

'''
만약에 시간의 벽을 벗어나는 경우 -> 유일한 출구로 이어짐.
출구를 찾아야 됨. 
'''
sr, sc = None, None
wallexit = None
ed = None
wx, wy = None, None

# 시간의 벽 격자 찾기
for r in range(N):
    for c in range(N):
        if overall_map[r][c] == 3:
            sr, sc = r, c
            break
    if sr is not None and sc is not None:
        break
# 유일한 연결 출구 찾기
for x in range(sr-1, sr+M+1):
    for y in range(sc-1, sc+M+1):
        if x == sr-1 or x == sr+M or y == sc-1 or y == sc+M:
            if overall_map[x][y] == 0:
                # sr-1: 북 / sr+1: 남 / sc-1: 서 / sc+1: 동
                if x == sr-1:
                    ed = "N"
                    wx, wy = 0, y - sc + M, 
                elif x == sr+M:
                    ed = "S"
                    wx, wy = 3*M-1, y - sc + M, 
                elif y == sc-1:
                    ed = "W"
                    wx, wy = x - sr + M, 0
                elif y == sc+M:
                    ed = "E"
                    wx, wy = x - sr + M, 3*M-1
                wallexit = (wx, wy, x, y, ed) 
                # (wx,wy) : 시간의 벽 내에서, 출구랑 이어지는 좌표 위치 (overall_map 기준인 애를, folded_walls에서의 위치로 바꿔줌)
                # (x, y): 시간의 벽을 둘러싸는 애들 중에 유일하게 0인 곳의 위
'''
시간의 벽 안에서의 bfs 함수. 단순히 동.서.남.북 1씩 이동으로만 생각하면 안됨.
전개도로 펼친 걸 고려해야 하는데, 예를 들어 south 면에 있었는데 east면으로 옮겨가는 최단 경로의 경우, folded_walls에서의 좌표를 생각해야 함.
남-동 혹은 서-북은 그냥 (x,y)=>(y,x)로 바뀜
북-동 혹은 서-남은 (x, y) -> (3*M - 1 - y, 3*M - 1 - x)
'''
def check_side(x, y):
    if 0 <= x < M and M <= y < 2*M:
        face = "N"
    elif M <= x < 2*M and 0 <= y < M:
        face = "W"
    elif M <= x < 2*M and M <= y < 2*M:
        face = "T"
    elif M <= x < 2*M and 2*M <= y < 3*M:
        face = "E"
    elif 2*M <= x < 3*M and M <= y < 2*M:
        face = "S"
    return face

def wall_bfs():
    q = deque([(folded_tx, folded_ty, 0)])
    visited = set()
    visited.add((folded_tx, folded_ty))
    transfrorm = {0:"N", 1:"S", 2:"W", 3:"E"}

    while q:
        cx, cy, dist = q.popleft()
        if cx==wallexit[0] and cy==wallexit[1]:
            return dist
        # 상하좌우 순서
        for i, (dx, dy) in enumerate(zip([-1,1,0,0], [0,0,-1,1])):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<3*M and 0<=ny<3*M and (nx, ny) not in visited:
                if folded_walls[nx][ny] == 0:
                    q.append((nx, ny, dist+1))
                    visited.add((nx, ny))
                elif folded_walls[nx][ny] == 1:
                    continue
                elif folded_walls[nx][ny] == -1:
                    face = check_side(cx, cy)
                    if {face, transfrorm[i]} == {"S", "E"} or {face, transfrorm[i]} == {"W", "N"}:
                        tx, ty = cy, cx
                    elif {face, transfrorm[i]} == {"S", "W"} or {face, transfrorm[i]} == {"N", "E"}:
                        tx, ty = 3*M-1-cy, 3*M-1-cx
                    else: continue
                    if 0<=tx<3*M and 0<=ty<3*M and (tx, ty) not in visited and folded_walls[tx][ty] == 0:
                        q.append((tx, ty, dist+1))
                        visited.add((tx, ty))
                        
    return -1

answer = -1
ex, ey = exitt

def floor_bfs(sx, sy, cturn):
    q = deque([(sx, sy, cturn)])
    visited = set()
    visited.add((sx, sy))

    while q:
        cx, cy, turn = q.popleft()
        if (cx, cy) == (ex, ey):
            return turn
        
        for dx, dy in zip([-1,1,0,0], [0,0,-1,1]):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and (overall_map[nx][ny] == 0 or overall_map[nx][ny] == 4):
                if abnormal[nx][ny] <= turn+1:
                    continue
                else:
                    q.append((nx, ny, turn+1))
                    visited.add((nx, ny))
    return -1



''' wallexit = (wx, wy, x, y, ed) '''
# 가장 첫 단계: 초기 위치부터 (wx,wy까지 최단거리 구하기)
# 우선 초기 타임머신의 위치에서부터, (wx, wy) 까지의 최단 거리 구해야 함.
# 여기까지의 경로는 바뀔 일이 없음 (시간 이상 현상의 영향을 받을 일이 없음)
# 이 bfs는 (folded_tx, folded_ty) 부터 (wx,wy) 까지 bfs
# 최단거리 구해서 turn에 더하기
wall_turn = wall_bfs()

# 그 다음, 미지 공간 평면도로 진입하기 전에 (x,y)가 시간 이상 현상의 영향을 받았는지 확인
## abnormal을 돌면서, 지금 turn이 key로 나눈 나머지가 0인지 확인하고,
## 0이 아니면 다음 while 턴으로
curr_turn = wall_turn+1
sx, sy = wallexit[2], wallexit[3]
# 이미 sx,sy가 시간 이상 현상으로 인해 막히면 답은 -1
if curr_turn >= abnormal[sx][sy]:
    answer = -1
# 그렇지 않고 갈 수 있으면, 여기서부터 미지 공간 평면도(overall_map) bfs 시작
else:
    answer = floor_bfs(sx, sy, curr_turn)


print(answer)