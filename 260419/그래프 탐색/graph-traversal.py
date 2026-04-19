n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visited = [False]*(n+1)
ans = 0
def dfs(node):
    global ans
    for curr in range(2, n+1):
        if not visited[curr] and ((node, curr) in edges or (curr, node) in edges):
            ans += 1
            visited[curr] = True
            dfs(curr)

dfs(1)
print(ans)