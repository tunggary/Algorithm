#백준 14502번
#아이디어: combination 혹은 dfs로 벽을 세우고 완전 탐색

import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

N,M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
empty_space = []
virus_space = []
result = 0

for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      empty_space.append((i,j))
    elif graph[i][j] == 2:
      virus_space.append((i,j))
      
def bfs(visited,x,y):
  q = deque([(x,y)])
  
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<N and 0<=ny<M:
        if visited[nx][ny] == 0:
          q.append((nx,ny))
          visited[nx][ny] = 2
  
for i in combinations(empty_space, 3):
  visited = deepcopy(graph)
  for x,y in i:
    visited[x][y] = 1
  for x,y in virus_space:
    bfs(visited,x,y)
  count = 0
  for i in range(N):
    for j in range(M):
      if visited[i][j] == 0:
        count += 1
  result = max(result, count)
print(result)