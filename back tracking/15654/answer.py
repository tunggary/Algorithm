#백준 15652번
#아이디어: 백트래킹을 이용, dict 자료형을 이용해서 시간복잡도를 줄인다.

import sys

n,m = map(int, sys.stdin.readline().split())
number = sorted(map(int, sys.stdin.readline().split()))
array = {}

def dfs():
  if len(array) == m:
    print(' '.join(map(str, array.keys())))
    return
  for i in number:
    if i not in array:
      array[i] = i
      dfs()
      array.pop(i)
dfs()