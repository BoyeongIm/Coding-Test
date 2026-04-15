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
    time, score = heapq.heappop(bombsq) # 여기서 score가 지금 음수임
    if totaltime >= time:
        if totalscore - totalbomb[0][0] + (-score) > totalscore:
            # totalbomb에 넣을 때 양수로 만들어줬기 때문에, minscore는 양수임.
            minscore, t = heapq.heappop(totalbomb)
            totalscore -= minscore
            totalscore += (-score)
            # 그래서 totalbomb로 넣어줄 때는 -score로 넣어줘서, 양수로 만들어주기
            heapq.heappush(totalbomb, (-score, time))
    else:
        totaltime += 1
        totalscore += (-score)
        heapq.heappush(totalbomb, (-score, time))

print(totalscore)