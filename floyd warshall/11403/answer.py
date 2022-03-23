#백준 11403번
#아이디어: 모든 노드로 부터 모든 노드(자기자신 포함)까지 경로가 존재하는지 확인하는 것이므로 플로이드 와샬로 해결

import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1
        
for i in range(n):
  print(' '.join(map(str,graph[i])))