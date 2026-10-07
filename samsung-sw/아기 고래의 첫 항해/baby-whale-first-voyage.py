def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])
'''
바다: N*N, (i,j): 바다(0)이거나 지나갈 수 없는 암초(1)
아기 고래: (r,c) 에서 출발, 처음 바라보는 방향 d(1,2,3,4 = 상,하,좌,우)
    - 헤엄칠 수 있는 모든 바다를 탐험하는 것이 목표

1단계: 인접 탐험
    - 현재 위치에서 상하좌우 인접 칸 중, 방문하지 않은 바다 칸이 있다면 우선순위대로 한 칸 이동
        1. 현재 방향으로 직진
        2. 반시계 90도 회전 후 직진
        3. 시계 90도 회전 후 직진
        4. 180도 회전 후 직진
    - 이동한 방향으로 방향 갱신
    - 인접한 칸에 방문 가능한 바다가 없을 때까지 반복

2단계: 가장 가까운 바다로 이동
    - 아직 방문하지 않은 바다 칸 중 현재 위치에서 가장 가까운 칸을 찾아 이동
    - 이미 방문한 바다를 지나갈 수 있음
    - 가까운 (목적지) 칸이 여러 개라면: 행 번호 -> 열 번호 작은 칸
    - 선택한 목적지 칸까지 최단 거리로 이동.
        - 매 이동마다 선택한 칸까지의 거리가 1 줄어드는 인접 칸으로
        - 좌,하,우,상 순서로 우선순위
    - 도착 후 다시 1단계부터 반복
- 헤엄칠 수 있는 모든 바다를 방문하면 종료

방문하는 바다 칸의 위치를 방문 순서대로 출력
'''
from collections import deque
N,r,c,d = map(int, input().split())
ocean_grid = [list(map(int, input().split())) for _ in range(N)]
dirdict = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}    # 상하좌우
straight = {1:1, 2:2, 3:3, 4:4}
counterclock = {1:3, 2:4, 3:2, 4:1}
clock = {1:4, 2:3, 3:1, 4:2}
upsidedown = {1:2, 2:1, 3:4, 4:3}
priorities = [straight, counterclock, clock, upsidedown]

ocean_num = 0
for i in range(N):
    for j in range(N):
        if ocean_grid[i][j] == 0:
            ocean_num += 1
visited_ocean = set()
visited_ocean.add((r-1,c-1))

def get_dist(sx, sy):
    # distgrid = [[-1]*N for _ in range(N)]
    candidates = []
    q = deque([(sx, sy, 0)])
    visited = set()
    visited.add((sx, sy))
    while q:
        cx, cy, dist = q.popleft()
        # distgrid[cx][cy] = dist
        for dx, dy in dirdict.values():
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and ocean_grid[nx][ny] == 0:
                visited.add((nx, ny))
                if (nx, ny) not in visited_ocean:
                    candidates.append((nx, ny, dist+1))
                q.append((nx, ny, dist+1))
    sorted_candidates = sorted(candidates, key=lambda x:(x[2], x[0], x[1]))
    return sorted_candidates

def goal_dist(gx, gy):
    distgrid = [[-1]*N for _ in range(N)]
    q = deque([(gx, gy, 0)])
    visited = set()
    visited.add((gx, gy))
    while q:
        cx, cy, dist = q.popleft()
        distgrid[cx][cy] = dist
        for dx, dy in dirdict.values():
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and ocean_grid[nx][ny] == 0:
                visited.add((nx, ny))
                q.append((nx, ny, dist+1))
    return distgrid


def visit_next(sx, sy, sd):
    cx, cy, cd = sx, sy, sd
    while True: 
        impossible = 0
        for p in priorities:
            nd = p[cd]
            cdx, cdy = dirdict[nd][0], dirdict[nd][1]
            nx, ny = cx+cdx, cy+cdy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited_ocean and ocean_grid[nx][ny] == 0:
                visited_ocean.add((nx, ny))
                print(nx+1, ny+1)
                cx, cy, cd = nx, ny, nd
                break
            else:
                impossible += 1
        if impossible == 4:
            break
    return cx, cy, cd

def nearest_bfs(sx, sy, gx, gy):
    q = deque([(sx, sy, None)])
    visited = set()
    visited.add((sx, sy))
    dxs, dys = [0,1,0,-1], [-1,0,1,0]   # 좌하우상
    mapping = {1:3, 2:2, 3:4, 4:1}
    while q:
        cx, cy, cd = q.popleft()
        if cx==gx and cy==gy:
            print(gx+1, gy+1)
            visited_ocean.add((gx, gy))
            return gx, gy, cd
        for i, (dx, dy) in enumerate(zip(dxs, dys)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and ocean_grid[nx][ny] == 0:
                if goal_dgrid[cx][cy] - goal_dgrid[nx][ny] == 1:
                    visited.add((nx, ny)) 
                    q.append((nx, ny, mapping[i+1]))

print(r,c)
curr_x, curr_y, curr_d = r-1, c-1, d
while ocean_num > len(visited_ocean):
    # 인접 탐험 함수
    mid_x, mid_y, mid_d = visit_next(curr_x, curr_y, curr_d)
    goal = get_dist(mid_x, mid_y)

    if goal:
        # 가장 가까운 바다로 이동   
        goal_x, goal_y, gdist = goal[0]
        goal_dgrid = goal_dist(goal_x, goal_y)
        gx, gy, final_d = nearest_bfs(mid_x, mid_y, goal_x, goal_y)
        curr_x, curr_y, curr_d = gx, gy, final_d