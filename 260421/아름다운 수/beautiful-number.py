n = int(input())

# Please write your code here.
ans = 0
def add(l):
    if l == n:
        return 1
    cnt = 0
    for i in range(1,5):
        l += i
        if l <= n:
            cnt += add(l)
        else:
            break
        l -= i
    return cnt

ans += add(0)
print(ans)