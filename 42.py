g = int(input())
p = int(input())
data = []
parent = [0] * (g+1)

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
        
for i in range(1,g+1):
    parent[i] = i
        
for _ in range(p):
    data.append(int(input()))
    
result = 0
for i in data:
    find = find_parent(parent, i)
    if find == 0:
        break
    result += 1
    union_parent(parent, find, find-1)
        
print(result)
