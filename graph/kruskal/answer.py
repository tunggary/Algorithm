#이코테 288p
#최소 신장 트리: 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프 중 비용이 가장 적은 트리
#크루스칼 알고리즘: 최소 신장 트리의 알고리즘 중 하나

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a

#노드의 개수와 간선의 개수 입력 받기
v,e = map(int,input().split())
parent = [0] * (v+1)

#모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
  parent[i] = i

#모든 간선 정보 입력 받기
for _ in range(e):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

#cost를 key로 해서 오름차순 정렬
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
    
