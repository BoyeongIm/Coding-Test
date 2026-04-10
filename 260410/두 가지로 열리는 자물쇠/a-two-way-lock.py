N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def check(n1, n2):
    l, s = max(n1, n2), min(n1, n2)
    return min(N-l+s, l-s)

ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if check(a1, i) <= 2 and check(b1, j) <= 2 and check(c1, k) <= 2:
                ans += 1
            elif check(a2, i) <= 2 and check(b2, j) <= 2 and check(c2, k) <= 2:
                ans += 1
print(ans)