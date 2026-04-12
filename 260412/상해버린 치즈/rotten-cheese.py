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
check_cheese = []
for person, milk, time in zip(p, m, t):
    if person in sick.keys() and time < sick[person]:
        check_cheese.append((milk, time))

rotten = []
for milk, time in check_cheese:
    ok = True
    for person, sicktime in sick.items():
        if time < sicktime:
            ok = False
    if not ok:
        rotten.append(milk)

maxperson = 0
for milk in rotten:
    person = 0
    for i in range(D):      
        if m[i] == milk:
            person += 1
    maxperson = max(person, maxperson)

print(maxperson)