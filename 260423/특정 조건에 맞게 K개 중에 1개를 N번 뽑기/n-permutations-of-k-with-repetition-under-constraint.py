K, N = map(int, input().split())

# Please write your code here.
chosen = []
def choose(currnum):
    if currnum == N:
        for c in chosen:
            print(c, end=' ')
        print()
        return
    
    for n in range(1, K+1):
        if len(chosen) >= 2 and not(chosen[-2]==chosen[-1]==n):
            chosen.append(n)
            choose(currnum+1)
            chosen.pop()
        elif len(chosen) < 2:
            chosen.append(n)
            choose(currnum+1)
            chosen.pop()
    return

choose(0)