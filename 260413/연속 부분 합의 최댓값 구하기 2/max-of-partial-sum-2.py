n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
maxsum = -9999999
for i in range(n):
    now = max(a[i], now+a[i]) # 계속 더해 나갈지, 초기화할지
    maxsum = max(now, maxsum)
print(maxsum)