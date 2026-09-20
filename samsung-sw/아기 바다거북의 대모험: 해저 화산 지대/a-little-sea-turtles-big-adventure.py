'''
각 턴 구성
1단계: 바다거북 이동
    장애물: 산호초(1), 다른 바다거북, 화석
    우선순위: 우(0,1), 하(1,0), 좌(0,-1), 상(-1,0)
2단계: 화산 압력 증가 -- 모든 해저 화산 압력이 10씩 증가
3단계: 각 화산의 분출 임계치 이상이면 열기 분출
    1. P만큼 열기 발생 -> 상하좌우로 뻗어나감, 이동할 때마다 이전 칸 열기/2 만큼 전파
        산호초를 만나거나, 열기 값이 0이 되면 전파 중단
        한 칸에 모이면 열기 합산
    2. 현재 마그마 압력 + 전파된 열기 합쳐서 P넘으면 분출
    3. 모든 분출 종료: 살아있는 거북이 칸의 열기 합이 20 -> 화석
4단계: 열기 정보 초기화 (분출한 화산은 다 0)
'''
from collections import deque
N, M, K = map(int, input().split())
obstacle = [list(map(int, input().split())) for _ in range(N)]
heat = [[0]*N for _ in range(N)]
pressure = [[0]*N for _ in range(N)]
threshold = [[0]*N for _ in range(N)]
turtles = [tuple(map(int, input().split())) for _ in range(M)]
vol_loc = [tuple(map(int, input().split())) for _ in range(K)]
fossils = set()
answer = [-1]*M
dxs, dys = [0,1,0,-1], [1,0,-1,0]
success = 0

# 거꾸로 최종 도착지->출발지까지 거리 계산
def bfs(t_idx):
    dist = [[-1]*N for _ in range(N)]
    dist[N-1][N-1] = 0
    q = deque([(N-1, N-1)])
    t2 = set(turtles[:])
    t2.remove(turtles[t_idx])
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx,ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == -1 and obstacle[nx][ny] == 0:
                if (nx, ny) not in fossils and (nx, ny) not in t2:
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))
    return dist

for t in range(1, 101): # 100턴
    if success == M:
        break
    ''' 1단계 '''
    for idx, pos in enumerate(turtles):
        # 이미 처리된 거북이인 경우
        if pos is None:
            continue
        cx, cy = pos
        # 현재 거북이 위치에 대해서, 최종 도착지부터 현재 위치까지 각 지점마다 거리가 얼마나 되는지 전부 조사
        # 어느 방향이 최적인지 조사하기 위함
        curr_dist = bfs(idx)
        # 최종 도착지까지 도달할 수 없는 경우 넘어감 (현재 이동하지 않음)
        if curr_dist[cx][cy] == -1:
            pass
        else:
            for dx, dy in zip(dxs, dys):
                nx, ny = cx+dx, cy+dy
                # 이동한 위치랑, 현재 위치랑 최종까지의 거리가 1밖에 차이가 안난다면 최단 경로로 연결된다고 볼 수 있음
                if 0<=nx<N and 0<=ny<N and curr_dist[nx][ny] == curr_dist[cx][cy]-1:
                    # 이동
                    cx, cy = nx, ny
                    turtles[idx] = (cx, cy)
                    if cx == N-1 and cy==N-1:   # 도착 처리
                        success += 1
                        answer[idx] = t 
                        turtles[idx] = None
                    break
    ''' 2단계 '''
    for pos in vol_loc:
        x,y,p = pos
        pressure[x][y] += 10
    '''
    3단계: 각 화산의 분출 임계치 이상이면 열기 분출
    1. P만큼 열기 발생 -> 상하좌우로 뻗어나감, 이동할 때마다 이전 칸 열기/2 만큼 전파
        산호초를 만나거나, 열기 값이 0이 되면 전파 중단
        한 칸에 모이면 열기 합산
    2. 현재 마그마 압력 + 전파된 열기 합쳐서 P넘으면 분출
    3. 모든 분출 종료: 살아있는 거북이 칸의 열기 합이 20 -> 화석
    '''
    erupted = set()
    while True:
        vx, vy, h = -1, -1, 0
        eruption = set()
        for pos in vol_loc:
            x,y,p = pos
            h = p
            if pressure[x][y]+heat[x][y] >= p and (x,y) not in erupted:
                eruption.add(pos)
        if not eruption:
            break
        for vx, vy, h in eruption:
            heat[vx][vy] += h
            for dx, dy in zip(dxs, dys):
                cx, cy = vx, vy
                fire = h
                while 0<=cx+dx<N and 0<=cy+dy<N and obstacle[cx+dx][cy+dy] == 0 and fire > 0:
                    cx, cy = cx+dx, cy+dy
                    fire = fire//2
                    heat[cx][cy] += fire
            erupted.add((vx,vy))
    '''
    4단계: 열기 정보 초기화 (분출한 화산은 다 0)
    '''
    for i in range(N):
        for j in range(N):
            if (i,j) in turtles:
                idx = turtles.index((i,j))
                if heat[i][j] >= 20:
                    fossils.add((i,j))
                    turtles[idx] = None
            if (i,j) in erupted:
                pressure[i][j] = 0
            heat[i][j] = 0

for i in range(len(answer)):
    print(answer[i])