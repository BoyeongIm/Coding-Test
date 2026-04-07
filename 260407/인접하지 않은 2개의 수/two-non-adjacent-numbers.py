n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
maxsum = -sys.maxsize

for i in range(n-2):
    for j in range(i+2, n):
        summ = numbers[i]+numbers[j]
        maxsum = max(summ, maxsum)

print(maxsum)
