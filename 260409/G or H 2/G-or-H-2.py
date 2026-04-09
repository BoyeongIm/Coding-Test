n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]
from collections import Counter
# Please write your code here.
arr = ['.'] * max(pos)
for p, a in zip(pos, alpha):
    arr[p-1] = a
N = len(arr)
maxsize = -1
for start in range(N):
    for size in range(N-start+1):
        if arr[start] != '.' and arr[start+size-1] != '.':
            chunk = arr[start:start+size]
            cnt = Counter(chunk)
            if maxsize < size:
                if cnt['G'] > 0 and cnt['H'] > 0 and cnt['G'] != cnt['H']:
                    continue
                else:
                    maxsize = size-1


print(maxsize)