#코딩 테스트를 위한 라이브러리

#자신이 속한 집합의 루트를 찾는 함수(parent: list, x: number)
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#서로소 집합을 합치는 함수(parent: list, x: number, y: number)
def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x
