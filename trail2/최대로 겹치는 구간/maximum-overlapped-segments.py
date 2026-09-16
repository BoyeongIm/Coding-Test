n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines = [0] * 200
for s in segments:
    start, end = s
    for idx in range(start, end):
        lines[idx+100] += 1

print(max(lines))