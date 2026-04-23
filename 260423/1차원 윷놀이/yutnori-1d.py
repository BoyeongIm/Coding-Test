n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

player = [1 for i in range(k)]
maxscore = -1
def play(idx):
    if idx == n:
        global maxscore
        score = 0
        for p in player:
            if p >= m:
                score += 1
        maxscore = max(maxscore, score)
        return
    for i in range(k):
        if player[i] >= m:
            continue
        player[i] += nums[idx]
        play(idx+1)
        player[i] -= nums [idx]
    return

play(0)
print(maxscore)