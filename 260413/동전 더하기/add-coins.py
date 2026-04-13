n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse=True)
ans = 0
for c in coins:
    if k <= 0:
        break
    ans += k//c
    k %= c
print(ans)
