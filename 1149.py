import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n):
  graph[i][0] = min(graph[i-1][1], graph[i-1][2]) + graph[i][0]
  graph[i][1] = min(graph[i-1][0], graph[i-1][2]) + graph[i][1]
  graph[i][2] = min(graph[i-1][1], graph[i-1][0]) + graph[i][2]
  
print(min(graph[n-1]))