def solution(n, edges):
  INF = int(1e9)
  graph = [[INF]*n for _ in range(n)]
  for edge in edges:
    graph[edge[0]][edge[1]] = 1
    graph[edge[1]][edge[0]] = 1
    
  for i in range(n):
    for j in range(n):
      if i == j:
        graph[i][j] = 0
  count = 0
  for i in range(n):
    for j in range(n):
      for k in range(n):
        graph[i][k] = min(graph[i][j] + graph[j][k], graph[i][k])
        
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if i != j and i != k and j != k:
          if graph[i][j] + graph[j][k] <= graph[i][k]:
            count += 1
  return count

print(solution(5,[[0,1],[0,2],[1,3],[1,4]]))