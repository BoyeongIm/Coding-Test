n, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2)]
# Please write your code here.
def move(board):
    temps = []
    for i in range(len(board)):
        temps.append(board[i][n-1])
        for j in range(n-1, 0, -1):
            board[i][j] = board[i][j-1]
    for i in range(len(temps)):
        board[1-i][0] = temps[i]

for _ in range(t):
    move(grid)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=' ')
    print()