def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])

def compute_dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)
'''
미로 N*N 크기 격자, 좌상단 (1,1)
- 빈칸(이동가능), 벽(이동 불가, 1~9 내구도, 회전 시 내구도 1 깎임, 0이 되면 빈칸)
- 출구: 여기에 도달하면 즉시 탈출

1. 1초마다 모든 참가자는 한 칸씩 움직임.
    - 두 위치의 최단거리: 맨해튼 거리
    - 동시에 움직임. 상하좌우 가능, 벽이 없는 곳으로 이동 (상하 방향 우선)
    - 움직인 칸은, 현재 머물러 있떤 칸보다 출구까지의 최단 거리가 가까워야 함.
    - 움직일 수 없으면 안움직이고, 한 칸에 두명 이상 가능

2. 이동 다 끝나면 미로 회전
    - 한명 이상의 참가자+출구 포함 가장 작은 정사각형 (2개 이상이면, r -> c 작은거 우선)
    - 시계방향 90도 회전 후 내구도 1씩 깎임

K초 동안 반복, 그 전에 다 탈출하면 게임 끝
- 게임이 끝났을 때의 모든 참가자들의 이동 거리 합과 출구 좌표 출력
'''
N,M,K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]     # 0 빈칸, 1~9 벽 내구도
ppl_list = []
escaped = set()     # 탈출하면 여기에 ppl_list 인덱스 저장하자
for _ in range(M):
    r,c = map(int, input().split())
    ppl_list.append((r-1, c-1))
er, ec = map(int, input().split())
# 미로 그리드에 -1로 출구 표시
maze[er-1][ec-1] = -1
exiit = (er-1, ec-1)
distsum = 0

# 각 참가자별로 움직일 수 있는 칸 찾는 함수
# final_d = find_dir(i, ppl_list)
# ppl_list 업데이트, 탈출하는 애 있으면 escaped 업데이트
# 움직일 수 있으면 새로운 좌표를, 불가능하면 None 리턴하도록해서 None이 아니면 distsum도 업데이트
def find_dir(maze, idx, ppl_list, exiit):
    if ppl_list[idx] is None:
        return None
    px, py = ppl_list[idx]
    final_nxy = None
    ex, ey = exiit
    mindist = compute_dist(px, py, ex, ey)

    for dx, dy in zip([-1,1,0,0],[0,0,-1,1]):
        nx, ny = px+dx, py+dy
        if 0<=nx<N and 0<=ny<N and maze[nx][ny] <= 0:
            dist = compute_dist(nx, ny, ex, ey)
            if dist < mindist:
                mindist = dist
                final_nxy = (nx, ny)
    return final_nxy

# 미로 회전 및 내구도 절감
# newgrid = rotate(maze, sx, sy, l)
def rotate_n_minus(maze, sx, sy, l, ppl_list):
    grid = [row[:] for row in maze]
    new_ppl = ppl_list[:]
    for r in range(l):
        for c in range(l):
            grid[sx+c][sy+l-1-r] = maze[sx+r][sy+c]
            if grid[sx+c][sy+l-1-r] > 0:
                grid[sx+c][sy+l-1-r] -= 1
            if (sx+r,sy+c) in ppl_list:
                for i, ppl in enumerate(ppl_list):
                    if ppl == (sx+r,sy+c):
                        new_ppl[i] = (sx+c, sy+l-1-r)
    return grid, new_ppl

## 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾아서 회전시키기 (newgrid 리턴하기)
## newgrid = find_minsquare(maze, ppl_list, exiit)
def find_minsquare(maze, ppl_list, exiit):
    ex, ey = exiit
    sx, sy = None, None
    minsize = None
    for l in range(2, N+1):
        for i in range(0, N-l+1):
            for j in range(0, N-l+1):
                gridSet = set()
                for x in range(i, i+l):
                    for y in range(j, j+l):
                        gridSet.add((x,y))
                if exiit not in gridSet:
                    continue
                else:
                    for (x,y) in gridSet:
                        if (x,y) in ppl_list:
                            sx, sy = i, j
                            minsize = l
                            break
                if minsize is not None:
                    break
            if minsize is not None:
                break
        if minsize is not None:
            break

    newgrid, newppl = rotate_n_minus(maze, sx, sy, l, ppl_list)
    return newgrid, newppl
                
for k in range(K):
    # 그 전에 다 탈출하면 게임 끝
    if len(escaped) == M:
        break
    for i in range(M):
        # 각 참가자별로 움직일 수 있는 칸 찾는 함수
        final_nxy = find_dir(maze, i, ppl_list, exiit)
        if final_nxy is not None:
            nx, ny = final_nxy
            if maze[nx][ny] == -1:
                escaped.add(i)
                ppl_list[i] = None
            else:
                ppl_list[i] = final_nxy
            distsum += 1
        else:
            continue
        # ppl_list 업데이트, 탈출하는 애 있으면 escaped 업데이트
        # 움직일 수 있으면 새로운 좌표를, 불가능하면 None 리턴하도록해서 None이 아니면 distsum도 업데이트
    # 미로 회전
    ## 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾아서 회전시키기 (newgrid 리턴하기)
    ## newgrid에 대해서 내구도 1씩 깎기

    if len(escaped) == M:
        break

    newgrid, newppl = find_minsquare(maze, ppl_list, exiit)
    maze = newgrid
    ppl_list = newppl
    for i in range(N):
        for j in range(N):
            if maze[i][j] == -1:
                # 회전 후 출구 업데이트
                exiit = (i,j)
                break

# 최종 출구 좌표 출력 시, 나오는 좌표에 1씩 더해서 출력하기
print(distsum)
ex, ey = exiit
print(ex+1, ey+1)