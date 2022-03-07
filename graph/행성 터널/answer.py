#이코테 398p
#아이디어: 크루스칼 알고리즘의 원리 정확히 파악. x,y,z 좌표의 값들을 따로 저장하고 sort하면 결국 가장 cost가 적은 값이 먼저 처리되고 union_parent됨

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
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
    
x.sort()
y.sort()
z.sort()
edges = []
for i in range(n-1):
    heapq.heappush(edges, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(edges, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(edges, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
    
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

result = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
    
