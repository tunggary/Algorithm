#백준 9663번
#아이디어: 백트래킹을 이용

import sys

N = int(sys.stdin.readline())

row = [0]*(N)
result = 0

def check(n):
  for i in range(n):
    if row[i] == row[n] or abs(row[n]-row[i]) == n - i:
      return False
  return True

def dfs(n):
  global result
  
  if n == N:
    result += 1
  else:
    for i in range(N):
      row[n] = i
      if check(n):
        dfs(n+1)
        
dfs(0)
print(result)
