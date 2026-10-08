def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])
'''
L*L 크기 체스판: (1,1) 시작, 빈칸/함정/벽 (0,1,2)
각 기사의 초기 위치 (r,c), h*w 크기의 직사각형 형태, 체력 k

1. 기사 이동
    - 상하좌우 중 하나로 한 칸 이동
    - 거기에 다른 기사가 있다면 함께 연쇄적으로 한 칸 밀려남
        - 벽을 마주칠 때까지 계속 밀려남
        - 만약에 하나라도 이동하려는 방향의 끝에 벽이 잇다면 모든 기사는 이동할 수 없음. 
    - 사라진 기사에게 명령을 내리면 아무 반응 X

2. 대결 대미지
    - 밀려난 기사들은 피해를 입게 됨
    - 이동한 영역의 h*w 직사각형 내에 놓여 있는 함정의 수만큼 체력이 깎임
    - 현재 체력 이상의 대미지를 받을 경우 체스판에서 사라지게 됨
    - 명령을 받은 기사는 피해를 입지 않음
'''
from collections import defaultdict, deque
d_dict = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}     # 상, 우, 하, 좌
L,N,Q = map(int, input().split())
chessboard = [list(map(int, input().split())) for _ in range(L)]    # 체스판 상태 기록 (빈칸, 함정, 벽)
knightdict = defaultdict(int)   # 기사별 체력 기록
damage = [0] * (N+1)            # 기사별 입은 데미지 기록
knightmap = [[0]*L for _ in range(L)]   # 영역 확인 그리드
knightlocs = defaultdict(list)  # 기사별 영역의 모든 좌표 기록

for i in range(1, N+1):
    r,c,h,w,k = map(int, input().split())
    knightdict[i] = k
    for x in range(r-1, r+h-1):
        for y in range(c-1, c+w-1):
            knightmap[x][y] = i
            knightlocs[i].append((x,y))

'''
### 밀쳐진 애들이 누군지 목록 반환하는 함수
moved_list = move_knight(i)
'''
def move_who(i, d):
    moved_list = [i]
    dx, dy = d_dict[d]
    # i번 기사의 스타트 위치에서부터 d방향으로 가면서 연결된 애들 모두 찾기
    q = deque([i])
    visited = set()
    visited.add(i)
    while q:
        k = q.popleft()
        for tx, ty in knightlocs[k]:
            # 명령 받은 방향 진행, 벽이 아니어야 하고!
            nx, ny = tx+dx, ty+dy
            # 범위체크 사실 필요 없음
            if 0<=nx<L and 0<=ny<L and chessboard[nx][ny] != 2:
                k2 = knightmap[nx][ny]
                # 겹치는(연결되는) 다른 조각이면! 추가
                if k2 > 0 and k != k2 and k2 not in visited:
                    q.append(k2)
                    visited.add(k2)
                    moved_list.append(k2)
            else:
                return []
    return moved_list

def move(moved_list, d):
    for k in moved_list:
        target = knightlocs[k]
        for tx, ty in target:
            knightmap[tx][ty] = 0
    dx, dy = d_dict[d]

    for k in moved_list:
        target = knightlocs[k]
        new_locs = []
        for tx, ty in target:
            nx, ny = tx+dx, ty+dy
            # knightlocs 업데이트
            new_locs.append((nx, ny))
        knightlocs[k] = new_locs
        for nx, ny in new_locs:
            knightmap[nx][ny] = k
    return

'''
# chessboard랑 knightmap 보면서, 지금 명령 받은 기사 i를 제외하고
# 밀쳐진 기사들이 데미지를 입었는지 확인히는 함수 (앞에서 만든 moved_list를 보면서)
# 이 함수에서, knightdict, knightlocs를 업데이트하고 damage도 업데이트 해야 함.
# get_damage(moved_list)
'''
def get_damage(i, moved_list):
    for k in moved_list:
        if k == i:
            continue
        trap = 0
        for tx, ty in knightlocs[k]:
            if chessboard[tx][ty] == 1:
                trap += 1
        if trap >= knightdict[k]:
            knightdict.pop(k)
            for tx, ty in knightlocs[k]:
                knightmap[tx][ty] = 0
            knightlocs.pop(k)
            damage[k] = 0
        else:
            damage[k] += trap
            knightdict[k] -= trap

for q in range(Q):
    i, d = map(int, input().split())
    # 체스판에서 사라진 기사에게 명령을 내리면 다음 턴으로
    if i not in knightdict.keys():
        continue
    else:
        ### 밀쳐진 애들이 누군지 목록 반환 필수
        moved_list = move_who(i, d)
        if moved_list==[]:
            continue

        # 기사 i를 포함해서 밀쳐지는 애들을 d방향으로 이동시키는 함수
        # chessboard를 보면서 knightmap, knightlocs 업데이트
        move(moved_list, d)
        # print_grid(knightmap)

        # chessboard랑 knightmap 보면서, 지금 명령 받은 기사 i를 제외하고
        # 밀쳐진 기사들이 데미지를 입었는지 확인히는 함수 (앞에서 만든 moved_list를 보면서)
        # 이 함수에서, knightdict, knightlocs를 업데이트하고 damage도 업데이트 해야 함.
        # 왜냐면 데미지가 0이 되면 사라져야 함
        get_damage(i, moved_list)

print(sum(damage))