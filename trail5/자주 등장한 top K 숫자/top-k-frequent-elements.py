n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
count = Counter(arr)
sorted_count = sorted(count.items(), key=lambda x:(-x[1], -x[0]))[:k]

dict_sorted = dict(sorted_count)
print(*dict_sorted.keys())