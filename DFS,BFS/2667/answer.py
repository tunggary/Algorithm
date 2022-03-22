#백준 2667번
#아이디어: bfs를 이용한 최단거리 구하기

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
visited = [[0]*n for _ in range(n)]
steps = [(-1,0),(1,0),(0,-1),(0,1)]
result = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().strip())))
  
def bfs(start, num):
  visited[start[0]][start[1]] = num
  count = 1
  q = deque()
  q.append((start[0], start[1]))
  
  while q:
    x,y = q.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
          visited[nx][ny] = num
          count += 1
          q.append((nx,ny))
  result.append(count)

num = 1      
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == 0:
      bfs((i,j), num)
      num += 1

result.sort() 
print(len(result))    
for i in result:
  print(i)