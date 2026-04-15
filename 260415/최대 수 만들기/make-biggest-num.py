n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from functools import cmp_to_key
def compare(x, y):
    x = str(x)
    y = str(y)
    if x*99999 > y*99999:
        return -1
    if x*99999 == y*99999:
        return 0
    else:
        return 1

arr.sort(key=cmp_to_key(compare))
ans = ''
for a in arr:
    ans += str(a)
print(int(ans))