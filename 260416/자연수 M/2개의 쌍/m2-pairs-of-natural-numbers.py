N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])

# Please write your code here.
l = []
for i in range(N):
    for _ in range(x[i]):
        l.append(y[i])
i, j = 0, N-1
minsum = 999999
l.sort()
while i < j:
    ssum = y[i] + y[j]
    minsum = min(minsum, ssum)
    i += 1
    j -= 1
print(minsum)