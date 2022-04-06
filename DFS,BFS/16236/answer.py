#백준 16236번
#아이디어: 구현 + 완전탐색 문제

import sys
from collections import deque
from heapq import heappush, heappop

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
size = 2
eat = 0
x,y = 0,0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      x,y = i,j
      graph[i][j] = 0

def bfs(i,j):
  visited = [[-1]*n for _ in range(n)]
  eatable = []
  q = deque([(i,j)])
  visited[i][j] = 0
  
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] == -1 and  graph[nx][ny] <= size:
          visited[nx][ny] = visited[x][y] + 1
          if 0 < graph[nx][ny] < size:
            heappush(eatable, (visited[nx][ny], nx, ny))
          q.append((nx,ny))
  
  if not eatable:
    return (-1,-1,-1)
  return heappop(eatable)

result = 0
while True:
  distance, nx, ny = bfs(x,y)
  if distance == -1:
    break
  graph[nx][ny] = 0
  result += distance
  eat += 1
  x,y = nx,ny
  if eat == size:
    size += 1
    eat = 0
    
print(result)
  