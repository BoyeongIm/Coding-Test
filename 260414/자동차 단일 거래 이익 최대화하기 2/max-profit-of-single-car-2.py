n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
maxprofit = 0
for i in range(n-1):
    for j in range(i+1, n):
        if price[i] < price[j]:
            maxprofit = max(maxprofit, price[j]-price[i])
print(maxprofit)