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
    
#정열된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left,bisect_right
def count_by_range(a, left, right):
  l_index = bisect_left(a, left)
  r_index = bisect_right(a, right)
  return r_index - l_index

#소수 판별 알고리즘
def is_prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True