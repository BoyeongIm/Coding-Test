N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
max_student = 0
P.sort()
for i in range(N):
    now_price = P[i]//2
    student = 1
    now_budget = B-now_price
    for j in range(N):
        if i==j:
            continue
        if now_budget > P[j]:
            now_budget -= P[j]
            student += 1
    max_student = max(student, max_student)
print(max_student)