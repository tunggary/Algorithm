import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# def find_sum(x,y,visited):
#   q = deque()
#   q.append((x,y,0,graph[x][y]))
#   visited[x][y] = True
#   max_value = 0
  
#   while q:
#     cx, cy, count, sum = q.popleft()
#     if count >= 4: 
#       break
#     if count == 3:
#       max_value = max(max_value, sum)
#     for i in range(4):
#       nx = cx + dx[i]
#       ny = cy + dy[i]
#       if 0<=nx<n and 0<=ny<m:
#         if not visited[nx][ny]:
#           visited[nx][ny] = True
#           q.append((nx,ny,count+1,sum+graph[nx][ny]))
#   return max_value
answer = 0
def dfs(x,y,count,sum):
  global answer
  if answer >= sum + max_value*(3 - count):
    return 
  if count == 3:
    answer = max(answer, sum)
  else:
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
          visited[nx][ny] = False

# def find_special(x,y):
#   global answer
#   sum = graph[x][y]
#   block = 0
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0<=nx<n and 0<=ny<m:
#       block += 1
#       sum += graph[nx][ny]
      
#   if block == 3:
#     answer = max(answer, sum)
  
#   if block == 4:
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       sum -= graph[nx][ny]
#       answer = max(answer, sum)
#       sum += graph[nx][ny]

#백트래킹

visited = [[False]*m for _ in range(n)]
max_value = max(map(max,graph))
for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i,j,0,graph[i][j])
    # find_special(i,j)
    visited[i][j] = False
  
print(answer)