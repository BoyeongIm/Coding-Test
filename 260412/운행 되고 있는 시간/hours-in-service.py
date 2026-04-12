n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
maxcnt = 0
for i in range(n):
    timetable = [0]*max(b)
    for j in range(n):
        if i==j:
            continue
        start, end = a[j], b[j]
        for k in range(start, end):
            if timetable[k] == 0:
                timetable[k] = 1
    timesum = sum(timetable)
    if maxcnt < timesum:
        maxcnt = timesum
print(maxcnt)