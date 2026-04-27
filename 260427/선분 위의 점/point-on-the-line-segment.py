n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
points.sort()
def lower_bound(q):
    l, r = 0, n-1
    while l<=r:
        mid = (l+r)//2
        if q <= points[mid]:
            r = mid-1
        else:
            l = mid+1
    return l

def upper_bound(q):
    l, r = 0, n-1
    while l<=r:
        mid = (l+r)//2
        if q < points[mid]:
            r = mid-1
        else:
            l = mid+1
    return r

for x, y in segments:
    left = lower_bound(x)
    right = upper_bound(y)
    print(right-left+1)