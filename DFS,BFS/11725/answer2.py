#백준 11725번
#아이디어: 트리 완전탐색(BFS)

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  visited[start] = True
  q = deque([start])
  
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        parent[i] = now
        visited[i] = True
        q.append(i)
    
bfs(1)  
for i in parent[2:]:
  print(i)
