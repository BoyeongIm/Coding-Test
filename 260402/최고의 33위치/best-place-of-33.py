n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
if n==3:
    answer = sum(1 if grid[i][j]==1 else 0 for i in range(n) for j in range(n))

else:
    for i in range(n-2):
        for j in range(n-2):
            val = 0
            rows = grid[i:i+3]
            for r in rows:
                val += sum(r[j:j+3])
            if val > answer:
                answer = val
print(answer)