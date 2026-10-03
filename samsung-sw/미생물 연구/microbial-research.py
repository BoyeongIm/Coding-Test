'''
1. 미생물 투입
    - 좌측 하단, 우측 상단이 주어지고 그 영역에 한 무리의 미생물 투입
    - 다른 미생물이 존재하면, 새로운 애들이 그 영역 내 미생물들을 잡아먹고 투입됨
        - 이때, 영역이 둘 이상으로 나눠지면 -> 전부 사라짐
2. 배양 용기 이동
    - 새로운 용기로 이동 (기존 용기에 한 마리도 존재하지 않을 때까지)
    - 기존 애들 중 영역이 가장 넓은 무리 선택 -> 그다음 우선순위는 먼저 투입된 애들
    - 형태 유지, 전체 범위 안 벗어나고, 다른 애들과 겹치지 않게. 
    - 최대한 x좌표 작은 위치 -> y좌표 작은 위치
    - 어디에도 둘 수 없으면 걔네는 사라짐
3. 실험 결과 기록
    - 상하좌우 맞닿은 면이 있는 무리끼리는 인접한 무리 (면이 둘 이상이어도 한번만 확인)
    - 모든 인접 무리 쌍을 확인해서, A영역 넓이 * B 영역 넓이 = 성과
    - 모든 성과의 합이 이 실험의 결과!
'''
from collections import defaultdict, deque
N, Q = map(int, input().split())    # 용기 크기, Q번 실험횟수이자 미생물 종 수
micros = defaultdict(set)           # 미생물 번호에 좌표들 저장
grid = [[0]*N for _ in range(N)]
new_grid = [[0]*N for _ in range(N)]

def check_removal(grid):
    dxs, dys = [1,0,0,-1], [0,1,-1,0]
    to_remove = []

    for i, cell in micros.items():
        if not cell:
            to_remove.append(i)
            continue
        visited = set()
        sr, sc = next(iter(cell))
        q = deque([(sr, sc)])  
        visited.add((sr,sc))
        while q:
            sr, sc = q.popleft()
            for dr, dc in zip(dxs, dys):
                nr, nc = sr+dr, sc+dc
                if 0<=nr<N and 0<=nc<N and (nr, nc) not in visited and grid[nr][nc] == i:
                    q.append((nr,nc))
                    visited.add((nr,nc))
        if len(visited) != len(micros[i]):
            to_remove.append(i)

    for micro_id in to_remove:
        for r,c in micros[micro_id]:
            grid[r][c] = 0
        micros.pop(micro_id)

for m in range(1, Q+1):
    r1, c1, r2, c2 = map(int, input().split())
    x1, y1, x2, y2 = N-c1-1, r1, N-c2, r2-1

    # 1. 미생물 투입
    # 행 범위: x2~x1+1, 열 범위: y1~y2+1
    affected = set()
    for i in range(x2, x1+1):
        for j in range(y1, y2+1):
            old = grid[i][j]
            if old != 0:
                affected.add(old)
                micros[old].remove((i,j))
            grid[i][j] = m
            micros[m].add((i,j))

    # 바꾸고 나서, 다른 미생물을 잡아먹은 적이 있다면 영역이 둘 이상으로 나눠진 게 있는지 확인
    if affected:
        check_removal(grid)

    # 2. 배양 용기 이동
    # x좌표가 작은 위치(=가장 작은 열번호) -> 그다음 y좌표가 가장 작은 위치(=가장 큰 행번호)
    sorted_micros = dict(sorted(micros.items(), key=lambda x:(-len(x[1]), x[0])))
    moved = set()
    for micro_id, cells in sorted_micros.items():
        base_r = max(r for r,c in cells)
        base_c = min(c for r,c in cells)
        new_cell = set()
        for c in range(N):
            for r in range(N-1, -1, -1):
                success = 0
                # (r,c) -> base 좌표의 새로운 도착점
                move_r = r-base_r
                move_c = c-base_c
                placed = False
                for curr_r, curr_c in cells:
                    nr = curr_r+move_r
                    nc = curr_c+move_c
                    if 0<=nr<N and 0<=nc<N and new_grid[nr][nc] == 0:
                        success +=1
                if success == len(cells):
                    placed = True
                    for curr_r, curr_c in cells:
                        nr = curr_r+move_r
                        nc = curr_c+move_c
                        new_grid[nr][nc] = micro_id
                        new_cell.add((nr, nc))
                    break
            if placed:
                moved.add(micro_id)
                micros[micro_id] = new_cell
                break
    # 어디에도 둘 수 없으면 걔네는 사라짐
    for micro_id in sorted_micros.keys():
        if micro_id not in moved:
            micros.pop(micro_id)

    # 3. 실험 결과 기록
    mnum = len(micros)
    result = 0
    if mnum == 1:
        print(0)
    else:
        checked = set()
        for i, cells in micros.items():
            done = False
            for r, c in cells:
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<N:
                        j = new_grid[nr][nc]
                        pair = tuple(sorted((i,j)))
                        if j != i and j > 0 and pair not in checked:
                            checked.add(pair)
                            a = len(micros[i])
                            b = len(micros[j])
                            result += a*b
        print(result)
                            
    grid = new_grid
    new_grid = [[0]*N for _ in range(N)]