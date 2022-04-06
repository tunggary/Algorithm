#백준 11725번
#아이디어: 트리 완전탐색(DFS), stack 메모리 엄청 잡아먹음

import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(n,p):
  parent[n] = p
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      dfs(i, n)
    
dfs(1,1)  
for i in parent[2:]:
  print(i)
