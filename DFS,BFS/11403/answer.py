#백준 11403번
#아이디어: 모든 노드로 부터 모든 노드(자기자신 포함)까지 경로가 존재하는지 확인하는 것인데
#각 노드에서 부터 완전 탐색(dfs,bfs)을 통해 갈 수 있는 모든 노드 확인

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
  #bfs
  # bfs(i,visited)
  # print()
  
  #dfs
  dfs(i,visited,0)
  print(' '.join(map(str, visited)))