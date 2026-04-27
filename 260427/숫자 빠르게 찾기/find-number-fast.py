n, m = map(int, input().split())
arr = list(map(int, input().split())) # size: n
queries = [int(input()) for _ in range(m)] # size: m

# Please write your code here.
for q in queries:
    l, r = 0, n-1
    ans = -1
    while l <= r:
        mid = (l+r) // 2
        if q == arr[mid]:
            ans = mid+1
            break
        elif q < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    print(ans)