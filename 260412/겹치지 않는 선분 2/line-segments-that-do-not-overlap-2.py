n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    a1, a2 = lines[i]
    crossed = False
    for j in range(n):
        if i==j:
            continue
        b1, b2 = lines[j]
        if (a1-b1) * (a2-b2) < 0: # 교차하는 조건!!
            crossed = True
            break
    if not crossed:
        ans += 1
print(ans)