n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for x, y in segments:
    ans = 0
    for p in points:
        if p < x or p > y:
            continue
        else:
            ans += 1
    print(ans)
