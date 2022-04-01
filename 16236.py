import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x,y = 0,0
size = 2
cur_eat = 0
time = 0
INF = int(1e9)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      x,y = i,j
      graph[i][j] = 0
      
def bfs(x,y):
  q = deque([(x,y)])
  visited = [[-1]*n for _ in range(n)]
  visited[x][y] = 0
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] == -1 and size >= graph[nx][ny]:
          visited[nx][ny] = visited[cx][cy] + 1
          q.append((nx,ny))
  return visited

def find_next(visited):
  min_value = INF
  x,y = None,None
  for i in range(n):
    for j in range(n):
      if  visited[i][j] != -1 and 0 < graph[i][j] < size:
        if visited[i][j] < min_value:
          min_value = visited[i][j]
          x,y = i,j
  return x,y,min_value

while True:
  nx,ny,take_time = find_next(bfs(x,y))
  if take_time == INF:
    break
  graph[nx][ny] = 0
  x,y = nx,ny
  cur_eat += 1
  time += take_time
  if cur_eat >= size:
    size += 1
    cur_eat = 0
print(time)