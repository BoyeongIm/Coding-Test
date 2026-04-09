N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
ans = 0
cnter = Counter(B)
for i in range(N-M+1):
    cnt = []
    for c in range(i, i+M):
        if A[c] in B:
            cnt.append(A[c])
    if Counter(cnt) == cnter:
        ans += 1
print(ans)