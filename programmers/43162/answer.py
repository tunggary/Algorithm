def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent,x,y):
  x = find_parent(parent,x)
  y = find_parent(parent,y)
  if x < y:
    parent[y] = parent[x]
  else:
    parent[x] = parent[y]

def solution(n, computers):
  parent = [i for i in range(n)]
  for i in range(n):
    for j in range(n):
      if computers[i][j] == 1:
        union_parent(parent,i,j)
        
  network = [0]*n
  for i in range(n):
    x = find_parent(parent, i)
    if network[x] == 0:
      network[x] = 1
  return sum(network)

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
      