N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
mincost = sys.maxsize
window = arr[:T]
for i in range(T, N):
    window.pop(0)
    window.append(arr[i])
    cnt = 0
    for w in window:
        if w == H:
            cnt += 1
    if cnt == T:
        mincost = 0
    else:
        cost = 0
        for i in range(T):
            cost += abs(window[i]-H)
        mincost = min(cost, mincost)
print(mincost)