n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

player = [1 for i in range(k)]
maxscore = -1
def play(idx):
    # 매번 점수 계산하면서 최대점수 갱신
    global maxscore
    score = 0
    for p in player:
        score += (p >= m)
    maxscore = max(maxscore, score)
    if idx == n:
        return
    for i in range(k):
        # 이미 m을 넘었다면 움직일 필요 없음.
        if player[i] >= m:
            continue
        player[i] += nums[idx]
        play(idx+1)
        player[i] -= nums [idx]

play(0)
print(maxscore)