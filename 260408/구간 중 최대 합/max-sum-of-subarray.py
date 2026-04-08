n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
maxsum = -sys.maxsize

for i in range(n-k+1):
    summ = sum(arr[i:i+k])
    maxsum = max(summ, maxsum)
print(maxsum)