#이코테 152p
#아이디어: 너비우선탐색으로 주변에 갈 수 있는 곳이 있는지 확인 후, queue에 넣고 최단경로(이전경로까지의 최단경로 + 1)를 graph에 입력한다.

from collections import deque

n,m = map(int,input().split())
graph = []
steps = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n):
  graph.append(list(map(int,input())))

def bfs(x,y):
  global n,m,graph,steps
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))

  return graph[n-1][m-1]

print(bfs(0,0))
