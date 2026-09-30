'''
먼지 / 먼지 없 / 물건(격자 값 -1)
- 먼지 양: 1~100
- 청소기 초기 위치에는 먼지 없음

1. 청소기 이동
    - 이동 거리가 가장 가까운 오염된 격자로 이동
    - 물건이나 청소기가 있는 곳은 지나갈 수 없음
    - 가장 가까운 격자가 여러 개일 경우 행 -> 열 번호 작은 게 우선
2. 청소
    - 바라보고 있는 방향 기준 현위치, 왼, 오, 위쪽 격자 청소 가능
    - 4개 중 먼지량이 가장 큰 방향에서 시작 (여러 개면 우->하->좌->상)
    - 최대 먼지량 20
3. 먼지 축적: 먼지가 있는 모든 격자에 5씩 추가
4. 먼지 확산
    - 깨끗한 격자에 주변 4방향 격자의 먼지 합을 10으로 나눈 만큼 확산
    - 소숫점 아래 수는 버림
5. 전체 공간의 총 먼지량 출력
위의 과정을 L번 반복, 테스트가 끝날 때마다 총 먼지량 출력 (L개)
'''
from collections import deque
N,K,L = map(int, input().split())
dust_board = [list(map(int, input().split())) for _ in range(N)]
robot_cleaner = [tuple(map(int, input().split())) for _ in range(K)]
cleaner_set = set()
for i, t in enumerate(robot_cleaner):
    r,c = t
    robot_cleaner[i] = (r-1, c-1)
    cleaner_set.add((r-1, c-1))

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and dust_board[x][y] != -1 and (x,y) not in cleaner_set

def bfs(x, y):
    q = deque([(x,y,0)])
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    visited = set()
    visited.add((x,y))
    best = None # 거리, 행, 열
    while q:
        cx, cy, dist = q.popleft()
        if best is not None and dist > best[0]:
            break   # BFS는 거리 오름차순으로 꺼내므로 더 볼 필요 없음
        if dust_board[cx][cy] > 0:
            cand = (dist, cx, cy)
            if best is None or cand < best: # 튜플로 해서 원소 순서대로 비교!! 대박
                best = cand
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, dist+1))
    return best

# 먼지 축적
def accum():
    for x in range(N):
        for y in range(N):
            if dust_board[x][y] > 0:
                dust_board[x][y] += 5

# 먼지 확산: 모든 깨끗한 격자에 대해 "동시에" 확산이 이루어지게 하려면, 원래의 dust_board를 순서대로 읽으면 안됨!!
# 원래 보드랑 따로 관리해야 하고, 그래서 지금 상태의 보드를 그대로 복사해서 새로운 보드에서 갱신시킨 다음에 이걸 리턴시켜야 함
# 근데 그냥 dust_board[:] 를 해버리면 얕은 복사여서 행이 공유됨. 행단위로 복사해야 됨.
def spread():
    new_b = [row[:] for row in dust_board]
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    for x in range(N):
        for y in range(N):
            if dust_board[x][y] == 0:
                dustsum = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny) and dust_board[nx][ny] > 0:
                        dustsum += dust_board[nx][ny]
                new_b[x][y] = dustsum//10
    return new_b

directions = [
    [(0,0), (0,1), (-1,0), (1,0)],
    [(0,0), (0,1), (0,-1), (1,0)],
    [(0,0), (0,-1), (-1,0), (1,0)],
    [(0,0), (-1,0), (0,-1), (0,1)]
] # 우, 하, 좌, 상

for i in range(L):
    targets = []
    for _ in range(K):
        rx, ry = robot_cleaner.pop(0)
        cleaner_set.discard((rx, ry))
        target = bfs(rx, ry)
        if target is None:
            robot_cleaner.append((rx, ry))
            cleaner_set.add((rx, ry))
            targets.append((rx, ry))
            continue
        dist, tx, ty = target
        robot_cleaner.append((tx, ty))
        cleaner_set.add((tx, ty))
        targets.append((tx, ty))
    
    for t in range(len(targets)):
        maxdust = -1
        cleand = None
        tx, ty = targets[t]
        for d in range(4):
            dustsum = 0
            for dx, dy in directions[d]:
                nx, ny = tx+dx, ty+dy
                if in_range(nx, ny):
                    if 0 < dust_board[nx][ny] < 20:
                        dustsum += dust_board[nx][ny]
                    elif dust_board[nx][ny] >= 20:
                        dustsum += 20
            if cleand is None or dustsum > maxdust:
                maxdust = dustsum
                cleand = d
        for dx, dy in directions[cleand]:
            nx, ny = tx+dx, ty+dy
            if in_range(nx, ny):
                if 0 < dust_board[nx][ny] <= 20:
                    dust_board[nx][ny] = 0
                elif dust_board[nx][ny] > 20:
                    dust_board[nx][ny] -= 20
    
    accum()
    dust_board = spread()
    total_sum = 0
    for x in range(N):
        for y in range(N):
            if dust_board[x][y] > 0:
                total_sum += dust_board[x][y]
    if total_sum == 0:
        print(0)
        break
    else:
        print(total_sum)
