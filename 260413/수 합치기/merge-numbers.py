n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 항상 최소값 2개를 빠르게 뽑을 수 있는 구조!!!
# 가장 작은 2개를 계속 관리할 수 있는 자료구조!! heapq!!
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