K, N = map(int, input().split())

# Please write your code here.

ans = []
def pick():
    if len(ans) == N:
        for a in ans:
            print(a, end=' ')
        print()
        return
    for i in range(1, K+1):
        ans.append(i)
        pick()
        ans.pop()
    return
    
pick()