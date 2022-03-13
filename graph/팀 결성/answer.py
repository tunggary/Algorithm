#이코테 298p
#아이디어: 서로소 집합을 이용해서 풀이

n,m = map(int, input().split())

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

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i
    
for _ in range(m):
    method, a, b = map(int, input().split())
    if method == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")