n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n): # 시작점
    for j in range(i, n): # 끝점
        summ = 0
        for k in range(i, j+1):
            summ += arr[k]
        mn = summ / (j-i+1)
        if mn in arr[i:j+1]:
            cnt += 1
print(cnt)