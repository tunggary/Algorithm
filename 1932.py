import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      graph[i][j] = graph[i-1][j] + graph[i][j]
    elif j == i:
      graph[i][j] = graph[i-1][j-1] + graph[i][j]
    else:
      graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]
      
print(max(graph[n-1]))