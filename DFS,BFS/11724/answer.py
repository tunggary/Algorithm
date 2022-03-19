#백준 11724번
#아이디어: bfs,dfs를 통한 완전 탐색

import sys 
sys.setrecursionlimit(100000)
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
visited = [False]*(n+1)
def dfs(n):
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      dfs(i)
      
def bfs(n):
  visited[n] = True
  q = [n]
  while q:
    now = q.pop(0)
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

count = 0
for i in range(1,n+1):
  if not visited[i]:
    # dfs(i)
    bfs(i)
    count += 1
print(count)