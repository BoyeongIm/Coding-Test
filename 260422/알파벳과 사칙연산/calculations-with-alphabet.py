expression = input()
l = len(expression)
# Please write your code here.
from collections import defaultdict
import sys
engdict = dict()
ops = {'+', '-', '*'}
ans = -sys.maxsize

def calc(op, cum, val):
    if op == '+':
        newresult = cum + val
    elif op == '-':
        newresult = cum - val
    elif op == '*':
        newresult = cum * val
    return newresult

def dfs(idx, result):
    global ans
    if idx >= l:
        ans = max(ans, result)
        return
    curr = expression[idx] 
    if idx > 0:
        op = expression[idx-1]
    else:
        op = '+'
    if curr in engdict:    
        val = engdict[curr]
        newresult = calc(op, result, val)
        dfs(idx+2, newresult)
    else:
        for i in range(1, 5):  
            engdict[curr] = i
            val = engdict[curr]
            newresult = calc(op, result, val)
            dfs(idx+2, newresult)
            del engdict[curr]   
    return

dfs(0, 0)
print(ans)