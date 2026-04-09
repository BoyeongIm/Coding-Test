N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
ans = 0
cnterA = Counter(A[:M])
cnterB = Counter(B)

if cnterA == cnterB:
    ans += 1
for i in range(M, N):
    left = A[i-M]
    right = A[i]
    cnterA[left] -= 1
    if cnterA[left] == 0:
        del cnterA[left]
    cnterA[right] += 1

    if cnterA == cnterB:
        ans += 1

print(ans)