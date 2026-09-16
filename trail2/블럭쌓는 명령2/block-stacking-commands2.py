n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0]*(n+1)
for c in commands:
    start, end = c
    for i in range(start, end+1):
        blocks[i] += 1

print(max(blocks))