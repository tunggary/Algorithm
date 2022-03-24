from collections import deque
import sys
m,n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

def check():
  value = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        return -1
      value = max(value, graph[i][j])
  return value - 1

def bfs():  
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 0 or graph[nx][ny] > graph[cx][cy] + 1:
           graph[nx][ny] = graph[cx][cy] + 1
           q.append((nx,ny))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i,j))
bfs()

print(check())
        
    