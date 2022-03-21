import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
graph = []
steps = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().strip())))
  
visited = [[0]*m for _ in range(n)]
def bfs(start):
  visited[start[0]][start[1]] = 1
  q = deque()
  q.append((start[0],start[1]))
  
  while q:
    x,y = q.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny] == 0 and not graph[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx,ny))
          
bfs((0,0))
print(visited[n-1][m-1])