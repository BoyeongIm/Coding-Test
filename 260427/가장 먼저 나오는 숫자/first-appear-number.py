n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
for q in query:
    l, r = 0, n-1
    idx = -1
    while l<=r:
        mid = (l+r) // 2
        if q <= arr[mid]:
            idx = mid
            r = mid-1
        else:
            l = mid+1
    if arr[idx] == q:
        print(idx+1)
    else:
        print(-1)