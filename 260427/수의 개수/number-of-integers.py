n, m = map(int, input().split())
arr = list(map(int, input().split())) # n개
queries = [int(input()) for _ in range(m)] # m개

# Please write your code here.
def lower_bound(target):
    l, r = 0, n-1
    minidx = n
    while l<=r:
        mid = (l+r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            if arr[mid] == target:
                minidx = min(minidx, mid)
            r = mid - 1 
    return minidx

def upper_bound(target):
    l, r = 0, n-1
    maxidx = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] <= target:
            if arr[mid] == target:
                maxidx = max(maxidx, mid)
            l = mid+1
        else:
            r = mid-1
    return maxidx

for q in queries:
    minidx, maxidx = lower_bound(q), upper_bound(q)
    if maxidx == -1 or minidx == n:
        print(0)
    else:
        print(maxidx-minidx+1)