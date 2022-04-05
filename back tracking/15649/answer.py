#백준 15649번
#아이디어: 백트래킹, 즉 DFS에서 구할려는 답과 상관이 없을때 더이상 recursion 하지 않고 뒤로 돌아가 다른 경우를 탐색

import sys

n,m = map(int, sys.stdin.readline().split())
array = {}

def dfs():
  if len(array) == m:
    print(' '.join(map(str, array.keys())))
    return
  for i in range(1,n+1):
    if i not in array:
      array[i] = i
      dfs()
      array.pop(i)
dfs()