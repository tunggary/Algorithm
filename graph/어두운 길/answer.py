#이코테 43p
#아이디어: 최소신장트리를 구하는 문제로 kruskal 알고리즘을 이용하면 해결할 수 있다.

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

n, m = map(int, input().split())
parent = [0]*n
for i in range(n):
    parent[i] = i
    
graph = []
total = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
    total += cost
    
graph.sort()

result = 0
while graph:
    cost, a, b = graph.pop(0)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(total - result)