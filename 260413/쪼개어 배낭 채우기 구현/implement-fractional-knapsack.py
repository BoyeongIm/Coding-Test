N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
weights, values = list(w), list(v)

# Please write your code here.
values_per_weight = []
for i in range(N):
    val, wei = values[i], weights[i]
    values_per_weight.append((i, val/wei))

values_per_weight.sort(lambda x:-x[1])
ans = 0
while M > 0:
    for idx, vpw in values_per_weight:
        totalw, totalv = weights[idx], values[idx]
        if totalw <= M:
            ans += totalv
            M -= totalw
        else:
            ans += vpw * M/totalw
            M -= totalw
        print(ans)
print(ans)