#백준 14500번
#아이디어: dfs를 활용하여 문제를 해결하고, 특이케이스의 경우도 dfs를 적절히 변형하여 적용시킨다. 또한 백트래킹을 이용하여 시간을 단축시킨다.

import sys
sys.setrecursionlimit(10000)
n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_block = max(map(max,graph))
result = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,count,sum):
  global result,max_block
  if sum + max_block*(3-count) <= result:
    return
  if count == 3:
    result = max(result, sum)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m:
      if not visited[nx][ny]:
        if count == 1:
          visited[nx][ny] = True
          dfs(x,y,count+1,sum+graph[nx][ny])
          visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx,ny,count+1,sum+graph[nx][ny])
        visited[nx][ny]= False
        
for i in range(n):
  for j in range(m):
    if i==0 and j==4:
      a = 3
    visited[i][j] = True
    dfs(i,j,0,graph[i][j])
    visited[i][j] = False
print(result)