import sys

n,m = map(int, sys.stdin.readline().split())
number = sorted(map(int, sys.stdin.readline().split()))
array = []
result = {}

def dfs():
  if len(array) == m:
    string = ' '.join(map(str,array))
    if string not in result:
      print(string)
      result[string] = 1
    return
  
  for i in number:
    if array:
      if array[-1] > i:
        continue
    array.append(i)
    dfs()
    array.pop()
    
dfs()