n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines_sorted = sorted(lines, key=lambda x:x[0])
cnt = n
for i in range(n-1):
    a1, a2 = lines_sorted[i]
    for j in range(i+1, n):
        b1, b2 = lines_sorted[j]
        if a2 > b2:
            cnt -= 2
print(cnt)