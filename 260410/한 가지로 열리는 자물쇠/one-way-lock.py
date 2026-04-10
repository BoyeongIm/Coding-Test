N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if abs(a-i) <= 2 or abs(b-j) <= 2 or abs(c-k) <= 2:
                ans += 1
print(ans)