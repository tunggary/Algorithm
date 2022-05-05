from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0

def bfs(x,y):
  q = deque([(x,y)])
  graph[x][y] = -1
  
  while q:
    cx,cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 0:
          graph[nx][ny] = -1
          q.append((nx,ny))
      
bfs(0,0)
while True:
  flag = True
  remove = []
  for x in range(n):
    for y in range(m):
      if graph[x][y] == 1:
        flag = False
        exposed = 0
        for i in range(4):
          if graph[x+dx[i]][y+dy[i]] == -1:
            exposed += 1
        if exposed >= 2:
          remove.append((x,y))
  for x,y in remove:
    graph[x][y] = 0
    bfs(x,y)
  if flag:
    break
  result += 1

print(result)