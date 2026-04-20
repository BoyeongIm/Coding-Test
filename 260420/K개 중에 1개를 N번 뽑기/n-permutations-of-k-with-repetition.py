K, N = map(int, input().split())

# Please write your code here.

ans = []
def pick(num):
    if len(ans) == N:
        for a in ans:
            print(a, end=' ')
        print()
        return
    for i in range(1, K+1):
        ans.append(i)
        pick(i+1)
        ans.pop()
    return
    
pick(1)