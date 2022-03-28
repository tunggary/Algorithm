#백준 7569번
#아이디어: bfs에 대한 정확한 이해가 필요함

import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

def check():
  max_day = 0
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 0:
          return -1
        max_day = max(max_day,graph[i][j][k])
  return max_day - 1

def bfs():
  while q:
    z,x,y = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0<=nx<n and 0<=ny<m and 0<=nz<h:
        if graph[nz][nx][ny] == 0:
          q.append((nz,nx,ny))
          graph[nz][nx][ny] = graph[z][x][y] + 1

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        q.append((i,j,k))

bfs()
print(check())