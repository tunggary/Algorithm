#백준 1629번
#아이디어: 분할 정복 거듭제곱

import sys

a,b,c = map(int, sys.stdin.readline().split())

def dfs(n):
  if n == 0:
    return 1
  x = dfs(n//2)
  if n % 2 == 0:
    return (x*x)%c
  else:
    return (x*x*a)%c
  
print(dfs(b))
