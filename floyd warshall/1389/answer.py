#백준 1389번
#아이디어: 모든 점에서 다른 모든점까지의 최단거리를 구하는 문제이므로 플로이드 와샬로 해결

import sys
n,m = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j] = 0
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0
sum_value = INF
for i in range(1,n+1):
  value = sum(graph[i][1:])
  if value < sum_value:
    sum_value = value
    result = i
print(result)