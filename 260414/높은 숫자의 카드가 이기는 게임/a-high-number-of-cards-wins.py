N = int(input())
B = [int(input()) for _ in range(N)]

# Please write your code here.
Bset = set(B)
A = [i+1 for i in range(2*N) if i+1 not in Bset]
A.sort()
B.sort()
i, j = 0, 0
score = 0
while i<N and j<N:
    if A[i] > B[j]:
        j += 1
        score += 1
    i += 1
print(score)