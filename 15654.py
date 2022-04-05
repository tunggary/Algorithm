import sys

N,M = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()
array = []

def dfs():
  global N,M
  if len(array) == M:
    print(' '.join(map(str, array)))
    return
  for i in number:
    if i not in array:
      array.append(i)
      dfs()
      array.pop()
      
dfs()