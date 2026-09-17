n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
cnt = Counter(arr)
ans = 0
for a in arr:
    if k-a == a:
        ans+= cnt[k-a]-1
    else:
        ans += cnt[k-a]
    cnt[a] -= 1

print(ans)