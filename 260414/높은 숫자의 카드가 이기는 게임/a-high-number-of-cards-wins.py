N = int(input())
B = [int(input()) for _ in range(N)]

# Please write your code here.
cards = [i+1 for i in range(2*N)]
A = [c for c in cards if c not in B]
A.sort()
B.sort()
i, j = 0, 0
score = 0
while i<N and j<N:
    if A[i] > B[j]:
        i += 1
        j += 1
        score += 1
    else:
        i += 1
print(score)