import heapq

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
x = []
y = []
z = []
for i in range(1,n+1):
    a,b,c = map(int, input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
    
x.sort()
y.sort()
z.sort()
graph = [] 
for i in range(n-1):
    heapq.heappush(graph, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(graph, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(graph, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))


parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

result = 0
while graph:
    cost, a, b = heapq.heappop(graph)
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a != parent_b:
        union_parent(parent, a, b)
        result += cost

print(result)