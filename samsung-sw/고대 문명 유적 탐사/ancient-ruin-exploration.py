'''
5*5 격자 형태, 유물 조각은 총 7종류 (1~7)

1. 탐사 진행
    - 3*3 격자를 선택해 회전시킬 수 있음 (시계 방향 90, 180, 270)
    90°  : (c, N-1-r)
    180° : (N-1-r, N-1-c)
    270° : (N-1-c, r)
    - 선택된 격자는 항상 회전을 진행
    (회전 목표)
    1: 유물 1차 획득 가치를 최대화
    2: 여러 가지인 경우, 회전 각도가 가장 작은 방법
    3: 그래도 여러 가지라면 열 작은 경우 -> 행 작은 경우

2. 유물 획득
    - 유물 1차 획득: 3개 이상 연결된 경우, 유물이 되어 사라짐. 가치는 모인 조각의 개수와 같음
        - 사라진 자리에는, 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생겨남
        - 열번호 작은 순 -> 행번호 큰 순
        - 이후부터는 남은 숫자부터 순서대로 사용
    - 유물 연쇄 획득: 새로 생겨난 이후에도 조각들이 3개 이상 연결될 수 있음.
        - 앞과 같은 방식으로 조각이 모여 유물이 되고 사라짐.
        - 사라진 위치에 또 생김
        - 더 이상 3개 이상 연결되는 애들이 없을 때까지 반복

위의 과정을 K번의 턴에 걸쳐 진행
각 턴마다 획득한 유물 가치의 총합 출력
그런데 K번 진행 못했어도, 획득 불가능했으면 모든 탐사는 그 즉시 종료
'''
from collections import deque, defaultdict
K, M = map(int, input().split())
relics_grid = [list(map(int, input().split())) for _ in range(5)]
walls = list(map(int, input().split()))
centers = [(1,1), (2,1), (3,1), (1,2), (2,2), (3,2), (1,3), (2,3), (3,3)]
dxs, dys = [1,0,-1,0], [0,-1,0,1]

def connected_bfs(grid):
    connected = set()
    for i in range(5):
        for j in range(5):
            sx, sy = i, j
            comp = grid[sx][sy]
            visited = set()
            visited.add((i,j))
            q = deque([(i,j)])
            while q:
                cx, cy = q.popleft()
                if len(visited) >= 3:
                    for v in visited:
                        if v not in connected:
                            connected.add(v)
                for dx, dy in zip(dxs, dys):
                    nx, ny = cx+dx, cy+dy
                    if 0<=nx<5 and 0<=ny<5 and (nx, ny) not in visited and grid[nx][ny] == grid[cx][cy]:
                        visited.add((nx, ny))
                        q.append((nx, ny))
    return connected

def fillin(targets):
    sorted_targets = sorted(targets, key=lambda x:(x[1], -x[0]))
    for i, target in enumerate(sorted_targets):
        tx, ty = target
        relics_grid[tx][ty] = walls[i]
    new_walls = walls[len(sorted_targets):]
    return new_walls

def rotate_n_count(angle):
    maxv = -1
    maxp = None
    maxgrid = None
    for cr, cc in centers:
        new_grid = [row[:] for row in relics_grid]
        sr, sc = cr-1, cc-1
        for r in range(3):
            for c in range(3):
                if angle == 0:
                    # 3*3 내에서 90도 회전: (r,c) -> (c, 2-r)
                    nr, nc = c, 2-r
                elif angle == 1:
                    nr, nc = 2-r, 2-c
                else:
                    nr, nc = 2-c, r
                new_grid[sr+nr][sc+nc] = relics_grid[sr+r][sc+c]
        connected_group = list(connected_bfs(new_grid))
        connected_value = len(connected_group)
        if maxv < connected_value:
            maxv = connected_value
            maxp = (cr, cc)
            maxgroup = connected_group
            maxgrid = new_grid
    return maxv, maxp, maxgroup, maxgrid

answer = []
for _ in range(K):
    # 모든 중심좌표 돌면서 탐사 진행 및 회전시키는 함수
    ## 중심좌표 총 9개에 대해서 90, 180, 270 모두 진행
    ## 그럼 총 9*3 = 27번 (회전시킨 결과를 내놓게 하기)
    maxvalue = -1
    maxgroups = None
    maxgrid = None
    for i in range(3):
        value, pair, c_group, ngrid = rotate_n_count(i)
        # 그중 가치 최대화 (즉 연결된 애들 가장 많은 거)  -> 회전 각도 더 작은거
        ### 사라진 좌표들 받아오기? -> 그래서 이거 없으면, 즉시 종료할 수 있도록
        if maxvalue < value:
            maxvalue = value
            maxgroups = c_group
            maxgrid = ngrid
    
    relics_grid = maxgrid
    
    if not maxgroups:
        break
    
    # 유물 조각 사라지고 난 후, 새로운 조각들로 채우는 함수
    walls = fillin(maxgroups)

    # 이후, 유물 연쇄 획득 함수
    ## 그냥 돌면서 연결된 애들 찾기
    while True:
        connected_more = list(connected_bfs(relics_grid))
        if not connected_more:
            break
        ## 그럼 걔네 비우고 또 채워
        walls = fillin(connected_more)
        maxvalue += len(connected_more)

    answer.append(maxvalue)

for v in answer:
    print(v, end= " ")