'''
F: 신봉하는 음식 (T,C,M: 민트, 초코, 우유)
    - 이중조합: CM, TM, TC
    - 삼중조합: TCM
B: 신앙심
T일 동안 아침,점심,저녁 순서로 과정 반복
1. 아침 시간
    - 신앙심에 1 더해짐
2. 점심 시간
    - 인접한 학생들과 신봉 음식이 완전히 같은 경우에만 그룹 형성 (상하좌우)
    - 그룹 내에서 대표자 한 명 선정
        1. 신앙심이 가장 큰 사람
        2. 동일한 경우, 행번호 가장 작은 사람
        3. 그다음에는 열번호 가장 작은 사람
    - 대표자 제외 나머지는 각자 신앙심을 대표자에게 넘김
        - 즉 대표자의 신앙심은 그룹원 수 -1만큼 추가, 나머지는 1씩 감소
3. 저녁 시간
    - 대표자들이 신앙 전파 
    순서 1. 단일 음식: 민트, 초코, 우유
        2. 이중조합: 초코우유, 민트우유, 민트초코
        3. 삼중조합: 민트초코우유
    - 같은 그룹 내에서는 대표자 신앙심 높은 순 > 대표자 행번호 작은 순 > 대표자 열번호 작은 순
    - 전파자: 신앙심 B중 1만 남기고 나머지 간절함 x=B-1로 바꿔 전파에 사용
            전파 방향은 B를 4로 나눈 나머지에 따라 결정 (0,1,2,3: 상하좌우 방향으로 전파)
            전파 방향으로 한칸씩 이동하면서 전파 시도 (밖으로 나가거나 간절함이 0이 되면 전파 종료)
            전파 대상이 전파자와 같은 경우, 하지 않고 다음으로 진행
            다른 경우, 전파 진행
    **전파 과정**
    - 전파자의 간절함 x, 전파 대상의 신앙심 y
    x>y: 강한 전파 성공 -- 동일한 음식을 신봉하게 됨.
         간절함이 y+1 만큼 깎임. 0이 되면 전파 종료 전파 대상의 신앙심은 1 증가 (y+=1)
    x<=y: 약한 전파 성공 -- 전파한 음식의 모든 기본 음식에도 관심을 가지게 됨.
          모두 합친 음식을 신앙하게 됨. e.g., 민트 <= 초코우유, 그러면 민트초코우유를 신봉하게 됨.
    - 전파를 당한 애는 즉시 방어상태가 되어 당일에는 전파를 하지 않음. 추가로 전파를 받는 것은 가능

각 날의 저녁시간이 끝난 후, 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트 순서대로 각 신봉자들의 신앙심 총합 출력
'''
from collections import defaultdict, deque
N,T = map(int, input().split())
F_board = [list(input().strip()) for _ in range(N)]    # list(input().strip()) -> 공백 안껴있는 문자열을, 문자 하나하나로 나눠서 리스트로 저장
B_board = [list(map(int, input().split())) for _ in range(N)]
foodtype = [{"T","C","M"}, {"T","C"}, {"T","M"}, {"C","M"}, {"M"}, {"C"}, {"T"}]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]     # 상하좌우

def breakfast():
    for i in range(N):
        for j in range(N):
            B_board[i][j] += 1

# 인접한 학생들끼리 신봉 음식이 같은 경우 그룹 형성
def bfs(sx, sy, visited, gn):
    q = deque([(sx, sy)])
    comp = set(F_board[sx][sy])
    groups[gn] = [(B_board[sx][sy], sx, sy)]
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited and set(F_board[nx][ny]) == comp:
                q.append((nx, ny))
                visited.add((nx, ny))
                groups[gn].append((B_board[nx][ny], nx, ny))    

def lunch():
    visited = set()
    gn = 0
    for sx in range(N):
        for sy in range(N):
            if (sx, sy) not in visited:
                visited.add((sx, sy))
                # 그룹 형성
                bfs(sx, sy, visited, gn)
                gn += 1
    # 대표자 선정
    for i, gr in groups.items():
        sorted_gr = sorted(gr, key=lambda x:(-x[0], x[1], x[2]))
        n = len(gr)
        for j in range(n):
            b, x, y = sorted_gr[j]
            if j==0:
                new_b = b+n-1
            else:
                new_b = b-1
            B_board[x][y] = new_b
            sorted_gr[j] = (new_b, x, y)   
        groups[i] = sorted_gr
        foodt = len(F_board[sorted_gr[0][1]][sorted_gr[0][2]])
        representatives[foodt].append(sorted_gr[0])

def dinner():
    # representatives를 key 크기로 오름차순 정렬해줘야 하는 이유: 단일-이중-삼중 순서로 진행해야 하기 때문
    for i, replist in sorted(representatives.items(), key=lambda x:x[0]):
        # 아래 정렬은 같은 그룹 내에서의 순서를 위함
        sorted_replist = sorted(replist, key=lambda x:(-x[0], x[1], x[2]))
        for rep in sorted_replist:
            # 시작 전파자
            sb, sx, sy = rep
            if delivered[sx][sy]:
                continue
            B_board[sx][sy] = 1
            f_belief = F_board[sx][sy]  # 전파할 음식
            x = sb-1    # 전파 대상의 간절함
            dx, dy = dxs[sb % 4], dys[sb % 4]   # 전파 방향
            cx, cy = sx, sy
            while x > 0:
                nx, ny = cx + dx, cy + dy   # 전파 대상                
                if not (0<=nx<N and 0<=ny<N):
                    break
                target = F_board[nx][ny]
                # 전파 대상이 전파자와 신봉 음식이 완전히 같은 경우에는, 전파를 하지 않고 바로 다음으로 진행
                if set(f_belief) == set(target):
                    cx, cy = nx, ny
                    continue
                # 다른 경우 전파 진행
                y = B_board[nx][ny]
                if x > y:   # 강한전파
                    F_board[nx][ny] = f_belief
                    x -= (y+1)
                    B_board[nx][ny] += 1
                else:   # 약한 전파 
                    target_set = set(target)
                    deliver_set = set(f_belief)
                    target_set = target_set | deliver_set
                    update = ""
                    for f in target_set:
                        update += f
                    F_board[nx][ny] = update
                    B_board[nx][ny] += x
                    x = 0
                delivered[nx][ny] = True
                cx, cy = nx, ny

for _ in range(T):
    delivered = [[False]*N for _ in range(N)]
    breakfast()
    groups = defaultdict(list)
    representatives = defaultdict(list)
    lunch()
    dinner()
    answer = ''
    for fs in foodtype:
        bsum = 0
        for i in range(N):
            for j in range(N):
                if set(F_board[i][j]) == fs:
                    bsum += B_board[i][j]
        answer += str(bsum)+" "
    print(answer)