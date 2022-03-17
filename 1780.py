from sys import stdin

n = int(stdin.readline())
graph = []
for _ in range(n):
  graph.append(list(map(int, stdin.readline().split())))
  
def check(row, col, n):
  data = graph[row][col]
  for i in range(n):
    for j in range(n):
      if graph[row+i][col+j] != data:
        return None
  return data
  
result = [0,0,0]
def dfs(row, col, n):
  data = check(row, col, n)
  if data == -1:
    result[0] += 1
  elif data == 0:
    result[1] += 1
  elif data == 1:
    result[2] += 1
  else:
    dfs(row,col,n//3)
    dfs(row+n//3,col,n//3)
    dfs(row+2*n//3,col,n//3)
    dfs(row,col+n//3,n//3)
    dfs(row+n//3,col+n//3,n//3)
    dfs(row+2*n//3,col+n//3,n//3)
    dfs(row,col+2*n//3,n//3)
    dfs(row+n//3,col+2*n//3,n//3)
    dfs(row+2*n//3,col+2*n//3,n//3)
    
dfs(0,0,n)
    
for i in result:
  print(i)