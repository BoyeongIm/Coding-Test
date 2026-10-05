'''
N*N 크기의 마을 (도로 0, 도로 아니면 1)
메두사 집: (sr, sc) 공원: (er, ec) -- 항상 도로 위에 있음. 도로만 다닐 수 있음.
M명의 전사들이 잡으러 옴 (각각 (ri, ci)): 최단경로로 이동, 어느 칸이든 이동 가능

1. 메두사의 이동
    - 도로를 따라 한 칸 이동
    - 공원까지 최단 경로 (우선순위: 상, 하, 좌, 우)
        - 경로 없을 수도 있음
    - 메두사가 이동한 칸에 전사가 있을 경우, 전사가 메두사의 공격을 받고 사라짐

2. 메두사의 시선
    - 상, 하, 좌, 우 방향 하나 선택해서 바라봄
    - 시야각 90도: 현재 위치 기준, 대각선까지 쭉+그 밑 영역 전부
    - 시야각 안에 있어도, 다른 전사에 가려져 있다면 보이지 않음
    - 메두사가 본 애들은 돌로 변해서 현재 턴에서는 움직일 수 없고, 턴 종료 시에 풀림

    (메두사와 마주치는 전사에 의해 가려지는 영역)
    - 전사가 메두사와 같은 행/열 (직선 방향) 에 있다면 곧게 뻗은 한 줄이 사라짐
    - 대각 방향이라면 삼각형으로 

    - 메두사는 전사를 가장 많이 볼 수 있는 방향을 바라봄. 여러 개라면, 상하좌우 우선순위

3. 전사들의 이동
    - 메두사를 향해 최대 두 칸까지 이동. 같은 칸 공유 가능
    (1) 거리를 줄일 수 있는 방향으로 한 칸 이동 (상하좌우 우선순위)
    (2) 한칸 더 이동 (좌우상하 우선순위)
    - 두 번 다 시야 범위 안으로는 이동 불가능

4. 전사의 공격
    - 메두사와 같은 칸에 도달한 전사는 공격
    - 그러나 이기지 못하고 사라지게 됨

- 전부 맨해튼 거리 기준
- 메두사가 공원에 도달할 때까지 매 턴마다 
  1. 해당 턴에서 모든 전사가 이동한 거리의 합
  2. 돌이 된 전사의 수
  3. 메두사를 공격한 전사의 수 출력
- 공원에 도착하는 턴에는 0을 출력하고 종료
'''
from collections import deque
N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())

warriors = list(map(int, input().split()))
warriors_list = []
wgrid = [[0]*N for _ in range(N)]
for i in range(0, 2*M, 2):
    warriors_list.append((warriors[i], warriors[i+1]))
    wgrid[warriors[i]][warriors[i+1]] += 1

village = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0,0,-1,1]
# 좌우상하
dxs2, dys2 = [0,0,-1,1],[-1,1,0,0]

def compute_distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def mtop_bfs():
    q = deque([([], sr, sc)])
    visited = set()
    visited.add((sr, sc))
    while q:
        path, cx, cy = q.popleft()
        if (cx, cy) == (er, ec):
            return path

        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and village[nx][ny] == 0:
                visited.add((nx, ny))
                q.append((path+[(nx, ny)], nx, ny))
    return -1

def make_view(tr, tc, i):
    view_grid = [[False]*N for _ in range(N)]
    rorder = 0
    corder = 0
    # 시야 만들기
    if i == 0:
        # tr-1 행부터 첫 행까지 (거꾸로)
        for r in range(tr-1, -1, -1):
            rorder += 1
            start, end = tc-rorder, tc+rorder+1
            if start < 0:
                start = 0
            if end >= N:
                end = N
            for c in range(start, end):
                view_grid[r][c] = True

    elif i == 1:
        # tr+1 행부터 끝까지
        for r in range(tr+1, N):
            rorder += 1
            start, end = tc-rorder, tc+rorder+1
            if start < 0:
                start = 0
            if end >= N:
                end = N
            for c in range(start, end):
                view_grid[r][c] = True

    elif i == 2:
        for c in range(tc-1, -1, -1):
            corder += 1
            start, end = tr-corder, tr+corder+1
            if start < 0:
                start = 0
            if end >= N:
                end = N
            for r in range(start, end):
                view_grid[r][c] = True
        
    else:
        for c in range(tc+1, N):
            corder += 1
            start, end = tr-corder, tr+corder+1
            if start < 0:
                start = 0
            if end >= N:
                end = N
            for r in range(start, end):
                view_grid[r][c] = True
    return view_grid

# 메두사의 시선: 시야각 범위 확인해서 바라본 전사의 수 (즉, 돌이 된 전사의 수) 와 시야범위 그리드, 돌이 된 애들의 리스트 리턴
# nw, ngrid, stones = view_angle(sr, sc, i)
# i=0,1,2,3 => 상,하,좌,우
def view_angle(tr, tc, i):
    view_grid = make_view(tr, tc, i)

    # 특정 전사에 의해 가려지는 범위 확인하고 False 시키기
    if i==0:
        for r in range(tr-1, -1, -1):
            for c in range(N):
                if wgrid[r][c] > 0:
                    if view_grid[r][c] and c == tc:
                        for nr in range(r-1, -1, -1):
                            view_grid[nr][c] = False
                    elif view_grid[r][c] and c != tc:
                        rorder = 0
                        for i in range(r-1,-1,-1):
                            rorder += 1
                            if c < tc:
                                start, end = c-rorder, c+1
                            elif c > tc:
                                start, end = c, c+rorder+1
                            if start < 0:
                                start = 0
                            if end >= N:
                                end = N
                            for j in range(start, end):
                                view_grid[i][j] = False

    elif i==1:
        for r in range(tr+1, N):
            for c in range(N):
                if wgrid[r][c] > 0:
                    if view_grid[r][c] and c == tc:
                        for nr in range(r+1, N):
                            view_grid[nr][c] = False
                    elif view_grid[r][c] and c != tc:
                        rorder = 0
                        for i in range(r+1, N):
                            rorder += 1
                            if c < tc:
                                start, end = c-rorder, c+1
                            elif c > tc:
                                start, end = c, c+rorder+1
                            if start < 0:
                                start = 0
                            if end >= N:
                                end = N
                            for j in range(start, end):
                                view_grid[i][j] = False
    
    elif i==2:
        for c in range(tc-1, -1, -1):
            for r in range(N):
                if wgrid[r][c] > 0:
                    if view_grid[r][c] and r == tr:
                        for nc in range(0, c):
                            view_grid[r][nc] = False
                    elif view_grid[r][c] and r != tr:
                        corder = 0
                        for j in range(c-1, -1, -1):
                            corder += 1
                            if r < tr:
                                start, end = r-corder, r+1
                            elif r > tr:
                                start, end = r, r+corder+1
                            if start < 0:
                                start = 0
                            if end >= N:
                                end = N
                            for i in range(start, end):
                                view_grid[i][j] = False
    
    else:
        for c in range(tc+1, N):
            for r in range(N):
                if wgrid[r][c] > 0:
                    if view_grid[r][c] and r == tr:
                        for nc in range(c+1, N):
                            view_grid[r][nc] = False
                    elif view_grid[r][c] and r != tr:
                        corder = 0
                        for j in range(c+1, N):
                            corder += 1
                            if r < tr:
                                start, end = r-corder, r+1
                            elif r > tr:
                                start, end = r, r+corder+1
                            if start < 0:
                                start = 0
                            if end >= N:
                                end = N
                            for i in range(start, end):
                                view_grid[i][j] = False

    
    stones = 0
    stonelist = []
    for x in range(N):
        for y in range(N):
            if view_grid[x][y]:
                stones += wgrid[x][y]
                for _ in range(wgrid[x][y]):
                    stonelist.append((x,y))
    return stones, view_grid, stonelist

'''
메인 동작 로직 흐름
'''
park_path = mtop_bfs()

# 최단 경로 없으면 -1 출력
if park_path == -1:
    print(-1)
else:
    for nx, ny in park_path:  
        # ** 1. 메두사의 이동 ** #  
        # 도로를 따라 한 칸 이동 (최단 경로를 따름)
        sr, sc = nx, ny

        # 공원에 도착하는 턴에는 0을 출력하고 종료
        if (sr, sc) == (er, ec):
            print(0)
            break

        # 이동한 칸에 전사가 있을 경우, 전사는 공격 받고 사라짐
        if wgrid[sr][sc] > 0:
            wgrid[sr][sc] = 0
            while (sr,sc) in warriors_list:
                warriors_list.remove((sr, sc))
        
        # ** 2. 메두사의 시선 ** #
        '''
        시야각 정하기: 전사를 가장 많이 볼 수 있는 방향인지 확인해야 함
        '''
        maxw = -1
        maxgrid = None     # 시야각 범위면 True 인 그리드
        maxstones = None
        for i in range(4): # 상,하,좌,우 순서
            # 시야각 범위 확인해서 바라본 전사의 수 (즉, 돌이 된 전사의 수) 와 시야범위 그리드, 돌이 된 애들의 리스트 리턴
            nw, ngrid, stones = view_angle(sr, sc, i)
            if nw > maxw:
                maxw = nw
                maxgrid = ngrid
                maxstones = stones
        # 돌이 된 애들을 전사로 유지해야 함
        nwlist = maxstones[:]
        attackers = 0
        all_distance = 0
        # ** 3. 전사들의 이동 ** #
        ### (wx,wy): 전사의 원래 위치 / (mx,my): 전사들의 두 번 이동 후 위치
        for wx, wy in warriors_list:
            # 돌이 된 애라면 이번 턴에서 움직일 수 없음
            if (wx, wy) in maxstones:
                continue
            min_dist = compute_distance(sr, sc, wx, wy)

            # 이동 후 위치를 우선 출발위치로 선언하기. 이동하지 않을 수도 있으니까
            mx, my = wx, wy

            # 1차 이동: 상하좌우
            for dx, dy in zip(dxs, dys):   
                nwx, nwy = wx+dx, wy+dy
                if 0<=nwx<N and 0<=nwy<N and not maxgrid[nwx][nwy]:
                    dist = compute_distance(sr, sc, nwx, nwy)
                    if dist < min_dist:
                        min_dist = dist
                        mx, my = nwx, nwy

            # 2차 이동: 좌우상하
            ## 출발지점은 1차에서 업뎃된 이후의 mx,my
            ## 2차 이동의 결과물을 저장할 변수를 따로 만들어놔야 함. 왜냐면 2차 이동 안할 수도 있는데, mx,my를 그대로 사용하면 
            cx, cy = mx, my
            for dx2, dy2 in zip(dxs2, dys2):
                # 1차 이동 끝난 애를 기준으로 이동해보기
                nwx2, nwy2 = mx+dx2, my+dy2
                if 0<=nwx2<N and 0<=nwy2<N and not maxgrid[nwx2][nwy2]:
                    dist = compute_distance(sr, sc, nwx2, nwy2)
                    if dist < min_dist:
                        min_dist = dist
                        # 2차 이동 완료하면 cx,cy 업뎃하기
                        cx, cy = nwx2, nwy2
            all_distance += compute_distance(wx, wy, cx, cy)

            # 이동 전 좌표에서는 빼줘야 함
            wgrid[wx][wy] -= 1
            # ** 4. 전사의 공격 ** #
            # 메두사와 같은 칸에 도달하면, 공격하고 사라져버림. 그러니까 그냥 바로 다음 턴 넘어가기
            if (cx, cy) == (sr, sc):
                attackers += 1
                continue
            # 그렇지 않으면, 우선 이동한 위치를 새롭게 그리드에 반영하기
            wgrid[cx][cy] += 1
            nwlist.append((cx, cy))
        
        # 새로운 애들로 warriors_list 즉 전사들의 좌표 집합 갱신하기
        warriors_list = nwlist

        # 해당 턴에서 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수를 공백을 사이에 두고 차례대로 출력
        print(all_distance, maxw, attackers)