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
    # A가 이길 수 있을 때만 j를 다음으로 넘기면서 B를 이길 수 있는 케이스 세기
    if A[i] > B[j]:
        j += 1
        score += 1
    # A 인덱스는 무조건 이동. 
    ## 둘다 정렬했을 때 가장 작은 것도 못이기면 어차피 A의 해당 카드로는 이길 수 없음.
    i += 1
print(score)