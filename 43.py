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

n,m = map(int, input().split())
graph = []
total_cost = 0
parent = [0]*n

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph.append((cost,a,b))
    total_cost += cost

for i in range(n):
    parent[i] = i

graph.sort()

sum = 0
while graph:
    cost,a,b = graph.pop(0)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        sum += cost

print(total_cost - sum)