from collections import defaultdict
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
curr = 0
cnt = defaultdict(lambda: [0, 0, '']) #[black, white]
for i in range(n):
    d, k = dir[i], x[i]
    if d == "R":
        for idx in range(curr, curr+k):
            cnt[idx][0] += 1
            cnt[idx][2] = 'b'
            # if cnt[idx][0] >= 2 and cnt[idx][1] >= 2:
            #     tiles[idx] = 'g'
            # else:
            #     tiles[idx] = 'b'
        curr += k-1
    else:
        for idx in range(curr, curr-k, -1):
            cnt[idx][1] += 1
            cnt[idx][2] = 'w'
            # if cnt[idx][0] >= 2 and cnt[idx][1] >= 2:
            #     tiles[idx] = 'g'
            # else:
            #     tiles[idx] = 'w'
        curr -= k-1

black, white, gray = 0, 0, 0
for b,w,last in cnt.values():
    if b>=2 and w>=2:
        gray += 1
    elif last == 'b':
        black += 1
    elif last == 'w':
        white += 1

print(white, black, gray)