import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(n, p):
  parent[n] = p
  for i in graph[n]:
    if parent[i] == 0:
      dfs(i, n)
dfs(1, 1)

for i in range(2,n+1):
  print(parent[i])