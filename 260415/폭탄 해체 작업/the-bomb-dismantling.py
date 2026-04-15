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
totaltime, totalscore = 0, 0
totalbomb = []
heapq.heapify(totalbomb)
while bombsq:
    time, score = heapq.heappop(bombsq)
    if totaltime >= time:
        if totalscore - totalbomb[0][0] + (-score) > totalscore:
            minscore, t = heapq.heappop(totalbomb)
            totalscore -= minscore
            totaltime -= 1
            totaltime += 1
            totalscore += (-score)
            heapq.heappush(totalbomb, (-score, time))
    else:
        totaltime += 1
        totalscore += (-score)
        heapq.heappush(totalbomb, (-score, time))

print(totalscore)