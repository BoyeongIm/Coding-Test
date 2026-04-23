n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict
player = defaultdict(int)
for i in range(1, k+1):
    player[i] = 1

maxscore = -1
def play(idx):
    if idx == n:
        global maxscore
        score = 0
        for p in player:
            if player[p] >= m:
                score += 1
        maxscore = max(maxscore, score)
        return
    for i in range(1, k+1):
        player[i] += nums[idx]
        play(idx+1)
        player[i] -= nums [idx]
    return

play(0)
print(maxscore)