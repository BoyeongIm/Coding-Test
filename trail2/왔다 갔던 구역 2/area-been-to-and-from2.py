n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
lines = [0]*2001
curr = 0
offset = 1000
for i in range(n):
    move = x[i]
    if dir[i] == "R":
        for idx in range(curr, curr+move):
            lines[idx+offset] += 1
        curr += move
    else:
        for idx in range(curr-move, curr):
            lines[idx+offset] += 1
        curr -= move

ans = 0
for n in lines:
    if n >= 2:
        ans += 1
print(ans)