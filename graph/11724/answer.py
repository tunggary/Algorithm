#백준 11724번
#아이디어: 서로소 집합을 이용해 부모노드가 다른 것의 갯수를 구한다.

import sys
n,m = map(int, sys.stdin.readline().split())
parent = [0]*(n+1)
for i in range(1,n+1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) 
  return parent[x]

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x
    
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  union_parent(parent,a, b)
    
result = set()
for i in range(1,n+1):
  data = find_parent(parent, i)
  result.add(data)
print(len(result))