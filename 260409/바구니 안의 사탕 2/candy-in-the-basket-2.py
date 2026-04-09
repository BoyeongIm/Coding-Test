N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
arr = [0] * max(pos)
for c, p in zip(candy, pos):
    arr[p-1] += c

window = sum(arr[:(2*K+1)])
maxsum = window

for i in range(K+1, len(arr)-K): 
    window -= arr[i-K-1]
    window += arr[i+K]
    maxsum = max(window, maxsum)
print(maxsum)