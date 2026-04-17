N = int(input())
from collections import deque
# Please write your code here.
q = deque([(N, 0)])
visited = [False] * (2*N)
visited[N] = True
while q:
    num, times = q.popleft()
    if num == 1:
        print(times)
        break
    for i in range(4):
        result = num
        if i == 0:
            result -= 1
        if i == 1:
            result += 1
        if i == 2 and result % 2 == 0:
            result //= 2
        if i == 3 and result % 3 == 0:
            result //= 3
        if 0 < result < 2*N and not visited[result]:
            visited[result] = True
            q.append((result, times+1))