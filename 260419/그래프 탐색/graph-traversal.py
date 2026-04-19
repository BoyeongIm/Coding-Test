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
    '''
    DFS는 "연결된 애들만 따라가는 구조"이다
    따라서:
    전체 노드를 도는 게 아니라 ❌
    현재 노드의 이웃만 본다 ⭕
    '''
    for nxt in graph[node]:
        if not visited[nxt]:
            ans += 1
            visited[nxt] = True
            dfs(nxt)
            
# 시작 노드는 방문 처리 해주기!!!!
visited[1]=True
dfs(1)
print(ans)