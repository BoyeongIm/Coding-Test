n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
from collections import defaultdict
tiles = defaultdict(str)
curr = 0
for i in range(n):
    d, move = dir[i], x[i]
    if d == "R":
        for idx in range(curr, curr+move):
            tiles[idx] = "R"
        curr += move-1
    else:
        for idx in range(curr, curr-move, -1):
            tiles[idx] = "L"
        curr -= move-1
    
black, white = 0,0
for t in tiles.values():
    if t == "L":
        white += 1
    else:
        black += 1

print(white, black)