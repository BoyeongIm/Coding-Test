import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)
min_diff = sys.maxsize
for i in range(N-1):
    for j in range(i+1, N):
        check = total-arr[i]-arr[j]
        min_diff = min(min_diff, abs(check-S))

print(min_diff)