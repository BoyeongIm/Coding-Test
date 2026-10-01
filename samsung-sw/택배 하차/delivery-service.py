'''
1. 택배 투입
    - 왼쪽 열의 위치 c, 가로 크기 w 세로 크기 h 택배번호 k
    - 중력에 의해 하단으로 떨어짐. 바닥이나 다른 짐을 만나면 멈춤
2. 택배 하차
    - 택배를 잡고 왼쪽으로 이동했을 때 부딪히지 않고 뺄 수 있는 애들부터
    - 여러 개인 경우, k가 작은 택배 먼저
    - 하차한 후에 밑으로 떨어질 수 있는 애들은 떨어짐
3. 2단계를 우측에서도 진행 (왼쪽 먼저 -> 그다음 오른쪽)
4. 택배를 모두 하차할 때까지 2,3의 과정을 반복
'''
import heapq
from collections import defaultdict
N, M = map(int, input().split()) # 그리드 크기, 택배 개수
packages = [tuple(map(int, input().split())) for _ in range(M)]
grid = [[0]*N for _ in range(N)]
blocks = defaultdict(tuple)
for p in packages:
    k,h,w,c = p
    blocks[k] = (c-1,w,h)

# 택배 투입
## 밑에서부터 올라오는 게 아니라, 밑으로 내려가면서 하나씩 체크해야 됨..
for bid, block in blocks.items():
    col, w, h = block
    start = None
    for x in range(0, N-h+1):
        check = True
        for i in range(h):
            for j in range(w):
                if grid[x+i][col+j] != 0:
                    check = False
                    break
            if not check:
                break
        if check:
            start = (x, col)
        else:
            start = (x-1, col)
            break
    sx, sy = start
    blocks[bid] = (sx, sy, w, h)
    for i in range(h):
        for j in range(w):
            if sx+i < N and sy+j < N:
                grid[sx+i][sy+j] = bid

def get_rid_of(sx, sy, w, h):
    for x in range(sx, sx+h):
        for y in range(sy, sy+w):
            grid[x][y] = 0


def get_down():
    sorted_blocks = dict(sorted(blocks.items(), key=lambda x:-(x[1][0]+x[1][3]-1)))
    for bid, block in sorted_blocks.items():
        sx, sy, w, h = block
        get_rid_of(sx, sy, w, h)
        bx, by = sx+h-1, sy
        stop = False
        while True:
            for i in range(w):
                if bx+1 < N and by+i < N and grid[bx+1][by+i] != 0:
                    stop = True
                    break
                elif bx+1 == N:
                    stop = True
                    break
            if stop:
                break
            bx += 1
        sx = bx-h+1
        blocks[bid] = (sx, sy, w, h)
        for x in range(sx, sx+h):
            for y in range(sy, sy+w):
                grid[x][y] = bid

def get_off_left():
    candidates = []
    heapq.heapify(candidates)
    for bid, block in blocks.items():
        sx, sy, w, h = block
        out = True
        for row in range(sx, sx+h):
            for col in range(sy-1, -1, -1):
                if grid[row][col] == 0:
                    continue 
                else:
                    out = False
                    break
            if not out:
                break
        if out:
            heapq.heappush(candidates, bid)
    target = candidates[0]
    print(target)
    sx, sy, w, h = blocks.pop(target)
    get_rid_of(sx, sy, w, h)

def get_off_right():
    candidates = []
    heapq.heapify(candidates)
    for bid, block in blocks.items():
        sx, sy, w, h = block
        out = True
        for row in range(sx, sx+h):
            for col in range(sy+w, N):
                if grid[row][col] == 0:
                    continue 
                else:
                    out = False
                    break
            if not out:
                break
        if out:
            heapq.heappush(candidates, bid)
    target = candidates[0]
    print(target)
    sx, sy, w, h = blocks.pop(target)
    get_rid_of(sx, sy, w, h)

while blocks:
    get_off_left()
    get_down()
    get_off_right()
    get_down()