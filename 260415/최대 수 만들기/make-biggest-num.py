n = int(input())
arr = [input() for _ in range(n)]
# Please write your code here.
from functools import cmp_to_key
def compare(x, y):
    if x+y > y+x:
        return -1
    if x+y == y+x:
        return 0
    else:
        return 1

arr.sort(key=cmp_to_key(compare))
print(''.join(arr))