N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

# sick_p, sick_t = [], []
sick = {}
for _ in range(S):
    person, time = map(int, input().split())
    sick[person] = time

# Please write your code here.
# 아픈 사람들 중에서 -> 아프게 한 원인을 먼저 찾고 -> 전체 검증
milks = [0] * (M+1)
for sickperson, sicktime in sick.items():
    # 아픈 사람 별로 한번씩 세야 함. 근데 어떤 사람이 같은 우유를 여러번 마실 수도 있기 때문에 이걸 고려해서
    # milks에 반영해야됨..
    drank = set()

    for i in range(D):
        if p[i] == sickperson and t[i] < sicktime:
            drank.add(m[i])

    for milk in drank:
        milks[milk] += 1

candidates = [i for i in range(len(milks)) if milks[i] == S]

ans = 0
for c in candidates:
    sick_p = set()
    for i in range(D):
        if m[i] == c:
            sick_p.add(p[i])
    ans = max(ans, len(sick_p))
print(ans)