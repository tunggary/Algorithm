from collections import deque
import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = True
  color = graph[x][y]
  
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny] == color and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx,ny))

normal = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      normal += 1
      
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'
      
redGreen = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      redGreen += 1
      
print(normal, redGreen)
      
