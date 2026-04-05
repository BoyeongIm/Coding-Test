n = int(input())
A = list(map(int, input().split()))

min_dist = 1000000
# Please write your code here.
for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(j-i) * A[j]
    min_dist = min(min_dist, dist)

print(min_dist)