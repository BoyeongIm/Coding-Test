expression = input()
l = len(expression)
# Please write your code here.
from collections import defaultdict
import sys
engdict = defaultdict(int)
ops = {'+', '-', '*'}
ans = -sys.maxsize

def dfs(op, idx, result):
    global ans
    if idx == l-1:
        ans = max(ans, result)
        return
    curr = expression[idx]
    for i in range(1, 5):   
        if engdict[curr] != 0:    
            if op == '+':
                newresult = result + engdict[curr]
            elif op == '-':
                newresult = result - engdict[curr]
            elif op == '*':
                newresult = result * engdict[curr]
            dfs(expression[idx+1], idx+2, newresult)
        else:
            engdict[curr] = i
            if op == '+':
                newresult = result + engdict[curr]
            elif op == '-':
                newresult = result - engdict[curr]
            elif op == '*':
                newresult = result * engdict[curr]
            dfs(expression[idx+1], idx+2, newresult)
            del engdict[curr]   
    return

dfs('+', 0, 0)
print(ans)