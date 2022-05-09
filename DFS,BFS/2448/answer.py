import sys

N = int(sys.stdin.readline())
graph = [[' ']*2*N for _ in range(N)]

def dfs(n, x, y):
  if n == 3:
    graph[x][y] = '*'
    graph[x+1][y-1] = '*'
    graph[x+1][y+1] = '*'
    for i in range(-2,3):
      graph[x+2][y+i] = '*'
    return
  
  dfs(n//2,x,y)
  dfs(n//2,x+n//2,y+n//2)
  dfs(n//2,x+n//2,y-n//2)
  
dfs(N,0,N-1)
for row in graph:
  print(''.join(row))