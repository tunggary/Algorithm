#백준 15652번
#아이디어: 백트래킹을 이용

import sys

n,m = map(int, sys.stdin.readline().split())
array = []

def dfs():
  if len(array) == m:
    print(' '.join(map(str, array)))
    return
  for i in range(1,n+1):
    if array and array[-1] > i:
      continue
    array.append(i)
    dfs()
    array.pop()
dfs()