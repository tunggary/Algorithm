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