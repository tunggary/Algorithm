#백준 7576번
#아이디어: bfs에 대한 이해 확실히 해야함

import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check():
  max_day = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        return -1
      max_day = max(max_day, graph[i][j])
  return max_day - 1

def bfs():
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 0:
          q.append((nx,ny))
          graph[nx][ny] = graph[x][y] + 1
           
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i,j))
      
bfs()
print(check())



