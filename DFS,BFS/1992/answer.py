#백준 1992번
#아이디어: dfs를 원리를 이용하여 해결 dfs 시작전 (, 끝난후 )를 넣는게 중요

import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def check(len,row,col):
  data = graph[row][col]
  for i in range(len):
    for j in range(len):
      if graph[row+i][col+j] != data:
        return None
  return data

def dfs(len,row,col):
  value = check(len,row,col)
  if value == 0:
    print("0", end="")
  elif value == 1:
    print("1", end="")
  else:
    half = len // 2
    print("(", end="")
    dfs(half,row,col)
    dfs(half,row,col+half)
    dfs(half,row+half,col)
    dfs(half,row+half,col+half)
    print(")", end="")
    
dfs(n,0,0)