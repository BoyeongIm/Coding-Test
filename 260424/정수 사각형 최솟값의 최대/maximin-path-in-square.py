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

if n == 1:
    ans = grid[0][0]

for i in range(1, n):
    for j in range(1, n): 
        dp[i][j] = max(
            # 위에서 오는 거랑 현재꺼 비교
            min(dp[i-1][j], grid[i][j]), 
            # 왼쪽에서 오는거랑 현재꺼 비교
            min(dp[i][j-1], grid[i][j])
            ) # 두 최솟값 중, 더 큰 값으로 갱신
        
print(dp[n-1][n-1])