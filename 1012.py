from collections import deque

steps = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(graph, row, col):
  q = deque()
  q.append((row,col))
  graph[row][col] = 0
  
  while q:
    now = q.popleft()
    for step in steps:
      nrow = now[0] + step[0]
      ncol = now[1] + step[1]
      if 0<=nrow<n and 0<=ncol<m:
        if graph[nrow][ncol] == 1:
          q.append((nrow, ncol))
          graph[nrow][ncol] = 0

for _ in range(int(input())):
  m,n,k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  for _ in range(k):
    col, row = map(int, input().split())
    graph[row][col] = 1
  
  count = 0
  for row in range(n):
    for col in range(m):
      if graph[row][col] == 1:
        bfs(graph, row, col)
        count += 1      
  print(count)