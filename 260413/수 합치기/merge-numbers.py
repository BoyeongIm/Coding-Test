n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq
heapq.heapify(arr)
mincost = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    cost = a+b
    mincost += cost
    heapq.heappush(arr, cost)
print(mincost)