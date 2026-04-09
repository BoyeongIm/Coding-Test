N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
window = arr[:T]
cost = 0
for w in window:
    cost += abs(w-H)
mincost = cost


for i in range(T, N):
    window.pop(0)
    window.append(arr[i])
    cost = 0
    for i in range(T):
        cost += abs(window[i]-H)
    mincost = min(cost, mincost)

print(mincost)