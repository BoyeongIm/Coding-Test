abilities = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations
import sys
comb = combinations(abilities, 3)
totalsum = sum(abilities)
mindiff = sys.maxsize
for c in comb:
    sum1 = sum(c)
    sum2 = totalsum-sum1
    mindiff = min(mindiff, abs(sum1-sum2))
print(mindiff)