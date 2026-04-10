arr = list(map(int, input().split()))

# Please write your code here.
import sys
totalsum = sum(arr)
INT_MAX = sys.maxsize
ans = INT_MAX
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            first = arr[i]
            second = arr[j]+arr[k]
            third = totalsum-first-second
            if first==second or second==third or first==third:
                break
            else:
                maxab = max(first, second, third)
                minab = min(first, second, third)
                ans = min(ans, maxab-minab)
if ans < INT_MAX:
    print(ans)
else:
    print(-1)