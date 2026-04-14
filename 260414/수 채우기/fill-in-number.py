n = int(input())

# Please write your code here.
cnt2 = 0
cnt5 = 0
if n % 2 == 1:
    while n >= 5 and n % 2 == 1:
        n -= 5
        cnt5 += 1
    cnt2 = n // 2
    n -= 2*cnt2
else:
    if (n // 5) % 2 == 1:
        cnt5 = n//5 -1
    else:
        cnt5 = n//5
    cnt2 = (n - cnt5*5) // 2
    n -= 5*cnt5+2*cnt2

if n == 0:
    print(cnt2+cnt5)
else:
    print(-1)