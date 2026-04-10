arr = list(map(int, input().split()))

# Please write your code here.
import sys
totalsum = sum(arr)
INT_MAX = sys.maxsize
ans = INT_MAX
for i in range(len(arr)):
    first = arr[i]
    newlist = arr[:i]+arr[i+1:]
    for j in range(len(newlist)-1):
        for k in range(j+1, len(newlist)):
            second = newlist[j]+newlist[k]
            third = totalsum-first-second
            if first==second or second==third or first==third:
                continue
            maxab = max(first, second, third)
            minab = min(first, second, third)
            ans = min(ans, maxab-minab)
if ans < INT_MAX:
    print(ans)
else:
    print(-1)