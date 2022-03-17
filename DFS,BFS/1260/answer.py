#백준 1260번
#아이디어: dfs,bfs를 통한 완전탐색

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  graph[i].sort()
    
def dfs(now, visited):
  print(now, end=" ")
  visited[now] = True
  for next in graph[now]:
    if not visited[next]:
      dfs(next, visited)
  
def bfs(start, visited):
  visited[start] = True
  q = [(start)]
  
  while q:
    now = q.pop(0)
    print(now, end=" ")
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        q.append(next)
        
dfs(v, [False]*(n+1))
print()
bfs(v, [False]*(n+1))