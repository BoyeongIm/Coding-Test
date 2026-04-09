N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(N-M+1):
    cnt = []
    for c in range(i, i+M):
        if A[c] in B:
            cnt.append(c)
    if len(cnt) == M:
        ans += 1
print(ans)