from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
gragh = [list(map(int, input().strip())) for _ in range(n)]
wall = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = int(1e9)

for i in range(n):
  for j in range(m):
    if gragh[i][j] == 1:
      wall.append((i,j))
      
def bfs(copy_graph):
  global n,m
  visited = [[-1]*m for _ in range(n)]
  visited[0][0] = 1
  q = deque([(0,0)])
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny] == -1 and copy_graph[nx][ny] == 0:
          visited[nx][ny] = visited[cx][cy]+1
          q.append((nx,ny))
  return visited[n-1][m-1]
            
# for x,y in wall:
#   copy_graph = deepcopy(gragh)
#   copy_graph[x][y] = 0
#   distance = bfs(copy_graph)
#   if distance > 0: 
#     result = min(result, distance)
result = bfs(gragh)
      
print(-1 if result == int(1e9) else result)