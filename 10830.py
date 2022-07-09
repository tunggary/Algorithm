import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def MatricMul(M1, M2):
  n = len(M1)
  Matric = [[0]*n for _ in range(n)]
  for row in range(n):
    for col in range(n):
      mul = 0
      for i in range(n):
        mul += (M1[row][i]*M2[i][col])
        Matric[row][col] = mul%1000
  return Matric

def dfs(Matric, m):
  if m == 1:
    for i in range(n):
      for j in range(n):
        Matric[i][j] %= 1000
    return Matric
  
  x = dfs(Matric, m//2)
  if m % 2 == 0:
    return MatricMul(x,x)
  else:
    return MatricMul(MatricMul(x,x),Matric)
  
for row in dfs(graph,m):
  print(*row)
  

  