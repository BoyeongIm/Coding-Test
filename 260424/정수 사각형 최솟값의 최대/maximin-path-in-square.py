n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0]*n for _ in range(n)]
import sys
def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], grid[i][0])
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], grid[0][j])
    
initialize()
ans = -sys.maxsize
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], grid[i][j])
        ans = max(ans, dp[i][j])

for i in range(1, n):
    for j in range(1, n):
        ans = max(ans, dp[i][j])
print(ans)