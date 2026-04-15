N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
score = [b[0] for b in bombs]
time_limit = [b[1] for b in bombs]

# Please write your code here.
import heapq
bombsq = []
for s, t in bombs:
    bombsq.append((t, -s))
heapq.heapify(bombsq)
totaltime = 0
totalscore = 0
while bombsq:
    time, score = heapq.heappop(bombsq)
    if totaltime >= time:
        continue
    totalscore += (-score)
    totaltime += 1
print(totalscore)