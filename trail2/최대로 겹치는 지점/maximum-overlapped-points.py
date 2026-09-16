n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines = [0]*101
for start, end in segments:
    for idx in range(start, end+1):
        lines[idx] += 1
print(max(lines))