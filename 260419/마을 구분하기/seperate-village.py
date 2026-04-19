n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False]*n for _ in range(n)]
villages = 0
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y):
    global person
    dxs, dys = [0,1,-1,0], [1,0,0,-1]
    for dx, dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            person += 1
            dfs(nx, ny)
people = []
for i in range(n):
    for j in range(n):
        # 1인 경우 즉 사람이 있는 경우! + visit 안한 경우
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            # 여기 안에 들어가서 마을이 어디까진지 세기
            person = 1
            dfs(i, j)
            people.append(person)
            # 빠져나오면 마을 하나 완성
            villages += 1
print(villages)
people.sort()
for p in people:
    print(p)