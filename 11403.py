import sys
from collections import deque
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
graph = [[]*n for _ in range(n)]
INF = int(1e9)

for i in range(n):
  row = list(map(int, sys.stdin.readline().split()))
  for j in range(n):
    if row[j] == 1:
      graph[i].append(j)
      
def bfs(start, visited):
  q = deque()
  q.append(start)
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        visited[i] = 1
        q.append(i)
  for i in range(n):
    print(visited[i], end=" ")
    
def dfs(now, visited, count): 
  if count != 0:
    visited[now] = 1
  for i in graph[now]:
    if not visited[i]:
      dfs(i,visited, count+1)
    

for i in range(n):
  visited = [0]*n
  # bfs(i,visited)
  # print()
  dfs(i,visited,0)
  print(' '.join(map(str, visited)))

# import sys

# n = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# for k in range(n):
#   for i in range(n):
#     for j in range(n):
#       if graph[i][k] and graph[k][j]:
#         graph[i][j] = 1
        
# for i in range(n):
#   print(' '.join(map(str,graph[i])))

