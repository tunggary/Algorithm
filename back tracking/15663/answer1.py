#백준 15663번
#아이디어: 같은 수가 여러개일때를 적절히 처리해야함

import sys

n,m = map(int, sys.stdin.readline().split())
number = sorted(map(int, sys.stdin.readline().split()))
count = [0]*(10001)
for i in number:
  count[i] += 1
result = {}
array = []

def dfs():
  if len(array) == m:
    string = ' '.join(map(str, array))
    if not result.get(string):
      print(string)
      result[string] = 1
    return
  
  for i in number:
    if count[i] > 0:
      array.append(i)
      count[i] -= 1
      dfs()
      count[i] += 1
      array.pop()
      
dfs()