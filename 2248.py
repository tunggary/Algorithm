import sys

n = int(sys.stdin.readline())
graph = [[' ']*2*n for _ in range(n)]

def dfs(x,y,n):
  if n == 3:
    graph[x][y] = '*'
    graph[x+1][y-1] = graph[x+1][y+1] = '*'
    for i in range(-2,3):
      graph[x+2][y+i] = '*'
  else:
    next = n//2
    dfs(x,y,next)
    dfs(x+next,y-next,next)
    dfs(x+next,y+next,next)
    
dfs(0,n-1,n)
for row in graph:
  print(''.join(row))