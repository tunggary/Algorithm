import sys

N,M = map(int, sys.stdin.readline().split())
array = []

def dfs():
  global N,M
  if len(array) == M:
    print(' '.join(map(str, array)))
    return
  for i in range(1,N+1):
    if array:
      if array[-1] > i:
        continue
    array.append(i)
    dfs()
    array.pop()
  
dfs()