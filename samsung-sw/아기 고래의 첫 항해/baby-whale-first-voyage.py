N, r, c, d = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]

'''
1. 인접 탐험
    - 이동 우선순위: 현재 방향 > 90도 반시계 > 90도 시계 > 180도 회전

2. (인접한 칸에 방문 가능한 바다가 없다면) 가장 가까운 바다로 이동
    - 암초 못지나감
    - 이미 방문한 바다 지나갈 수 있음
    - 가장 가까운 칸이 여러 개라면, 행 번호 > 열 번호 우선순위로 작은 칸 선택
    - 선택한 칸까지 최단 거리로 이동, 가능한 경로가 여러 개라면 좌>하>우>상 순서로 우선순위 
    - 마지막 이동 방향으로 바라보는 방향 갱신
'''
dirs = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)} # 상 하 좌 우
straight = {1:1, 2:2, 3:3, 4:4}
counterclock = {1:3, 3:2, 2:4, 4:1}
clock = {1:4, 4:2, 2:3, 3:1}
opposite = {1:2, 2:1, 3:4, 4:3}
priorities = [straight, counterclock, clock, opposite]

from collections import deque

# BFS & 주어진 지점부터 모든 지점까지의 거리를 저장한 2차원 배열 리턴
def get_dist(tx, ty):
    dist = [[-1]*N for _ in range(N)]
    directions = [[0]*N for _ in range(N)]
    dist[tx][ty] = 0
    q = deque([(tx, ty)])
    while q:
        cx, cy = q.popleft()
        for i, (dx, dy) in enumerate(zip(dxs, dys)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and dist[nx][ny]==-1 and ocean[nx][ny]==0:
                dist[nx][ny] = dist[cx][cy] + 1
                directions[nx][ny] = i
                q.append((nx, ny))
    return dist, directions

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

# 헤엄칠 수 있는 모든 바다를 방문하면 종료
while len(visited) < total_ocean:
    # 1단계: 우선순위대로 방문하지 않은 바다 칸으로 이동
    for p in priorities:
        ## 지금 우선순위 대로 회전해서 방향 바꾸기
        nd = p[cd]
        dx, dy = dirs[nd]
        nx, ny = cx+dx, cy+dy
        if 0<=nx<N and 0<=ny<N and ocean[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            cx,cy,cd = nx,ny,nd
            print(nx+1, ny+1)   
            break
    # 1단계에서 처리될 수가 없어서 (인접한 칸에 방문 가능한 바다가 없어서) 앞의 for문이 break로 끝나지 않았을 때 else로 처리하기
    else:
        ## 지금 현재 위치를 기준으로 가장 가까운 칸을 찾기 위해서, 현재 위치 기준 모든 위치까지의 거리 계산
        ## 이동할 타깃 위치를 찾는다 !!!
        dist, directions = get_dist(cx, cy)
        target = (99,-1,-1)    # cx,cy 기준으로 얼마나 떨어져있는지 거리와, 타겟 좌표
        for i in range(N):
            for j in range(N):
                # 암초가 아니면서 아직 방문하지 않은 바다만 방문할 수 있ㅇ므. 
                if ocean[i][j] == 0 and (i,j) not in visited and dist[i][j] != -1:
                    if dist[i][j] < target[0]:
                        target = (dist[i][j], i, j)
                    elif dist[i][j] == target[0]:
                        if target[1] > i:
                            target = (dist[i][j], i, j)
                        elif target[1] == i and target[2] > j:
                            target = (dist[i][j], i, j)

        tdistance, tx, ty = target
        cx, cy = tx, ty
        '''
        # get_dist bfs 코드에서 좌하우상 순서대로(0,1,2,3) 찾는데, 이게 미리 정의한 dirs랑은 다름. 
        그래서 그걸 맞춰주기 위해서, bfs에서 사용하는 순서에 맞게 매칭시켜줌. difs의 키와 올바르게 매칭시켜줌.
        즉, dirs에서는 키값이 3,2,4,1 이 순서대로 좌,하,우,상 인것
        '''
        cd = [3,2,4,1][directions[tx][ty]]  

        visited.add((cx, cy))    
        print(cx+1, cy+1)