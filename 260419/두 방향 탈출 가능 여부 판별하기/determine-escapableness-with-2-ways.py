n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*m for _ in range(n)]
def can_go(x, y):
    return 0<=x<n and 0<=y<m and grid[x][y] == 1

def dfs(x, y):
    # if x==n-1 and y==m-1:
    #     return True

    dxs = [1,0]
    dys = [0,1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)
    #         if dfs(nx, ny):
    #             return True
    # return False

visited[0][0] = 1
dfs(0,0)
print(visited[n-1][m-1])
# if dfs(0,0):
#     print(1)
# else:
#     print(0)

'''
그냥 visited로 도착부분만 확인할 수도 있음!!!!!
'''