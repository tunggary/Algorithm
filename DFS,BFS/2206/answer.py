#백준 2206번
#아이디어: 그래프에 상태를 하나 더 추가한다.

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[int(1e9)]*2 for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
  dist[0][0][0] = 1
  q = deque([(0,0,0)])
  while q:
    x,y,count = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 1 and count < 1:
          dist[nx][ny][1] = dist[x][y][0] + 1
          q.append((nx,ny,count+1))
        elif graph[nx][ny] == 0 and dist[nx][ny][count] > dist[x][y][count]+1:
          dist[nx][ny][count] = dist[x][y][count]+1
          q.append((nx,ny,count))
          
  result = min(dist[n-1][m-1])
  if result == int(1e9):
    result = -1
  return result
        
print(bfs())
