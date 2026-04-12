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
# print(check_cheese)

sick_people = set()
for c, time in check_cheese:
    for i in range(D):
        if m[i] == c and t[i] <= time:
            sick_people.add(p[i])
# print(sick_people)
print(len(sick_people))