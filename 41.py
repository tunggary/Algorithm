n,m = map(int, input().split())
graph = []
parent = [0]*(n+1)

for _ in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a 
        
for i in range(1,n+1):
    parent[i] = i
    
for i in range(n):
    for j in range(i+1):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

print(parent)
find = find_parent(parent, plan[0])
result = "YES"
for i in range(1, len(plan)):
    if find != find_parent(parent, plan[i]):
        result = "NO"
        break;
print(result)