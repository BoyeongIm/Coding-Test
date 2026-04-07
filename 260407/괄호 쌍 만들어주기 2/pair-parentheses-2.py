A = input()

# Please write your code here.
op = "(("
cl = "))"
n = len(A)
ans = 0
for i in range(n-2):
    if A[i:i+2] == op:
        for j in range(i, n-1):
            if A[j:j+2] == cl:
                ans += 1
print(ans)