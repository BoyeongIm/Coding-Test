n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
ans = 0

def dfs(node):
    global ans
    for nxt in graph[node]:
        if not visited[nxt]:
            ans += 1
            visited[nxt] = True
            dfs(nxt)
visited[1]=True
dfs(1)
print(ans)