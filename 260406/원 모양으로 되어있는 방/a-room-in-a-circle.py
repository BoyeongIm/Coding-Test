import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
people = sum(a)
mindist = sys.maxsize
for _ in range(n):
    dist = 0
    for j in range(n):
        dist += j * a[j]
    mindist = min(dist, mindist)
    temp = a[0]
    for k in range(n-1):
        a[k] = a[k+1]
    a[-1] = temp

print(mindist)