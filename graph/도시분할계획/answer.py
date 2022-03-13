#이코테
#아이디어: 크루스칼 알고리즘은 간선의 비용이 작은것부터 처리함으로 분리된 두 마을에서도 최소 신장트리는 분리되기 전과 같다. 
#따라서 최소신장트리를 구하고 그 간선중에서 가장 큰 값을 빼면 두 마을의 최소신장트리를 구할 수 있다.

import heapq
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, sys.stdin.readline().split())
graph = []
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
    
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    heapq.heappush(graph, (c,a,b))
    
sum = 0
max_value = 0
while graph:
    cost, a, b = heapq.heappop(graph)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_value = max(max_value, cost)
        sum += cost

print(sum - max_value)