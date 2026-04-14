n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
maxprofit = 0
'''
파는 시점 기준 최솟값과의 차이가 최대가 되는 순간을 구해야 함.
이전에 구했던 최솟값을 활용해서 계산.
'''
minprice = price[0]
for i in range(n):
    profit = price[i] - minprice
    maxprofit = max(profit, maxprofit)
    if price[i] < minprice:
        minprice = price[i]
print(maxprofit)