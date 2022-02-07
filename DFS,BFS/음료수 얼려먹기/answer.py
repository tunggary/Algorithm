#이코테 149p
#아이디어: 깊이우선탐색으로 인접한 0을 모두 탐색하여 방문표시를 하고 최초의 호출된 함수의 return을 True로 하여 하나의 영역이 증가하였음을 알려준다.

n, m = map(int,input().split())
graph = []
steps = [(-1,0),(1,0),(0,-1),(0,1)]
count = 0

for i in range(n):
  graph.append(list(map(int,input())))

def dfs(i, j):
  global steps,n,m,graph
  
  if i < 0 or i >= n or j < 0 or j >= m:
    return False
  
  if graph[i][j] == 0:
    graph[i][j] = 1
    for step in steps:
      dfs(i+step[0], j+step[1])
    return True
  else:
    return False

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1

print(count)
