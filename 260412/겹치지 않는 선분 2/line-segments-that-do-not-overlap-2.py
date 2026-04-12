n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines_sorted = sorted(lines, key=lambda x:x[0])
ans = 0
for i in range(n-1):
    a1, a2 = lines_sorted[i]
    crossed = False
    for j in range(i+1, n):
        b1, b2 = lines_sorted[j]
        if (a1-b1) * (a2-b2) < 0:
            crossed = True
            break
    if not crossed:
        ans += 1
print(ans)