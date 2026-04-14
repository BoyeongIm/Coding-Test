n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
maxprofit = 0
minprice = [price[0]] * n
for i in range(1,n):
    if price[i] < minprice[i-1]:
        minprice[i] = price[i]
    else:
        minprice[i] = minprice[i-1]
for i in range(n):
    profit = price[i] - minprice[i]
    maxprofit = max(profit, maxprofit)
print(maxprofit)