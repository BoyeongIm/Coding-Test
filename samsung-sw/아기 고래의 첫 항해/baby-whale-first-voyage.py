N, r, c, d = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]

'''
1. 인접 탐험
    - 이동 우선순위: 현재 방향 > 90도 반시계 > 90도 시계 > 180도 회전

'''
dirs = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)} # 상 하 좌 우
straight = {1:1, 2:2, 3:3, 4:4}
counterclock = {1:3, 3:2, 2:4, 4:1}
clock = {1:4, 4:2, 2:3, 3:1}
opposite = {1:2, 2:1, 3:4, 4:3}
priorities = [straight, counterclock, clock, opposite]

'''
2. (인접한 칸에 방문 가능한 바다가 없다면) 가장 가까운 바다로 이동
- 암초 못지나감
- 이미 방문한 바다 지나갈 수 있음
- 가장 가까운 칸이 여러 개라면, 행 번호 > 열 번호 우선순위로 작은 칸 선택
- 선택한 칸까지 최단 거리로 이동, 여러 개라면 좌>하>우>상 순서로 우선순위 
- 마지막 이동 방향으로 바라보는 방향 갱신
'''
from collections import deque

def get_dist(tx, ty):
    dist = [[-1]*N for _ in range(N)]
    dist[tx][ty] = 0
    q = deque([(tx, ty)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and dist[nx][ny]==-1 and ocean[nx][ny]==0:
                dist[nx][ny] = dist[cx][cy] + 1
                q.append((nx, ny))
    return dist


dxs, dys = [0,1,0,-1],[-1,0,1,0] # 좌 하 우 상
visited = set()
print(r, c)
visited.add((r-1,c-1))
cx,cy,cd = r-1,c-1,d
total_ocean = 0
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 0:
            total_ocean += 1

while len(visited) < total_ocean:
    for p in priorities:
        dx, dy = dirs[p[cd]]
        nx, ny = cx+dx, cy+dy
        nd = p[cd]
        if 0<=nx<N and 0<=ny<N and ocean[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            cx,cy,cd = nx,ny,nd
            print(nx+1, ny+1)   
            break
    else:
        dist = get_dist(cx, cy)
        target = (99,-1.-1)
        for i in range(N):
            for j in range(N):
                if ocean[i][j] == 0 and (i,j) not in visited and dist[i][j] != -1:
                    if dist[i][j] < target[0]:
                        target = (dist[i][j], i, j)
                    elif dist[i][j] == target[0]:
                        if target[1] > i:
                            target = (dist[i][j], i, j)
                        elif target[1] == i and target[2] > j:
                            target = (dist[i][j], i, j)

        td, tx, ty = target
        tdist = get_dist(tx, ty)
        while (cx, cy) != (tx, ty):
            for i in range(4):
                nx, ny = cx+dxs[i], cy+dys[i]
                if 0<=nx<N and 0<=ny<N and tdist[nx][ny] == tdist[cx][cy]-1:
                    cx, cy = nx, ny
                    cd = [3,2,4,1][i]
                    break
        visited.add((cx, cy))    
        print(cx+1, cy+1)