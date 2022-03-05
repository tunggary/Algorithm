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