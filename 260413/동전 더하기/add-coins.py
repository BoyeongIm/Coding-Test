n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse=True)
for c in coins:
    k %= c
    print(k)