n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum = arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
    
print(max_sum)