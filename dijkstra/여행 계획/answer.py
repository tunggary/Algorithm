#이코테 41번
#아이디어: 서로소 집합 알고리즘을 이용하여 해결하면 됨

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
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

result = 'YES'
param = find_parent(parent, plan[0])
for i in plan:
    if param != find_parent(parent, i):
        result = 'NO'
        break
print(result)