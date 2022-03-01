
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
        
n = int(input())
coordinate = []
for _ in range(n):
    x,y,z = map(int, input().split())
    coordinate.append((x,y,z))

graph = [] 
for i in range(n):
    for j in range(i, n):
        xi, yi, zi = coordinate[i]
        xj, yj, zj = coordinate[j]
        cost = min(abs(xi-xj), abs(yi-yj), abs(zi-zj))
        graph.append((cost, i, j))

graph.sort()

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

result = 0
while graph:
    cost, a, b = graph.pop(0)
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a != parent_b:
        union_parent(parent, a, b)
        result += cost

print(result)