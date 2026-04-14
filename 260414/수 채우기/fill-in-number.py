n = int(input())

# Please write your code here.
cnt = n // 5
end = False
## 5를 최대한 많이 쓰게 하고, 안되면 줄여나가는 방식으로 하기
while cnt >= 0:
    remain = n - 5*cnt
    if remain % 2 == 0:
        end = True
        print(cnt + remain//2)
        break
    cnt -=1
if not end:
    print(-1)