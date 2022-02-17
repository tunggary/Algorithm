#이코테 275p
#서로소 집합: 공통 원소가 없는 두 집합을 의미합니다.
#서로소 자료구조는 두 집합을 합치는 연산과 속한 집합의 root를 알려주는 연산이 있다.
#서로소 집합을 활용하여 사이클 판별 코드를 짤 수 있다.


#원소의 root를 찾음
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소의 root를 같게 해주는, 즉 하나의 집합으로 합쳐줌
def union_parent(parent, a, b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0]*(v+1)

#부모 테이블을 자기 자신으로 초기화
for i in range(1,v+1):
  parent[i] = i

#union 연산을 각각 실행
for i in range(e):
  a,b = map(int,input().split())
  union_parent(parent, a,b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1,v+1):
  print(find_parent(parent,i), end=" ")
