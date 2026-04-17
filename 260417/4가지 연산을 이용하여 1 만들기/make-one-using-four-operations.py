N = int(input())
from collections import deque
# Please write your code here.
def cal(i, num):
    if i == 0:
        return num-1
    if i == 1:
        return num+1
    if i == 2 and num % 2 == 0:
        return num//2
    if i == 3 and num % 3 == 0:
        return num//3
    return num
q = deque([(N, 0)])
visited = [False] * (2*N)
visited[N] = True
while q:
    num, times = q.popleft()
    if num == 1:
        print(times)
        break
    for i in range(4):
        result = cal(i, num)
        if not visited[result]:
            visited[result] = True
            q.append((result, times+1))