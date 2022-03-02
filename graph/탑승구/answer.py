#이코테 42p
#아이디어: 서로소 집합 알고리즘을 이용하면 해결할 수 있다.

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

g = int(input())
p = int(input())
airplane = []
for _ in range(p):
    airplane.append(int(input()))
    
parent = [0]*(g+1)
for i in range(1, g+1):
    parent[i] = i

result = 0
for maxGate in airplane:
    #자신이 들어갈 수 있는 가장 큰 gate에 들어가는 것을 원칙으로함
    currentGate = find_parent(parent, maxGate)
    #1번 게이트까지 꽉찬 경우
    if currentGate == 0:
        break
    #자신이 들어갔으므로 이후 같은 게이트에 들어올려 하면 자신보다 하나 작은 gate로 들어 갈 수 있게 한다.
    union_parent(parent, currentGate, currentGate-1)
    result += 1
print(result)