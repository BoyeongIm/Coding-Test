n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
maxsum = -9999999
for start in range(n):
    now = 0
    for end in range(start, n):
        now += a[end]
    maxsum = max(maxsum, now)
print(maxsum)