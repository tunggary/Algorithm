# import sys
# n,m = map(int, sys.stdin.readline().split())
# parent = [0]*(n+1)
# for i in range(1,n+1):
#   parent[i] = i

# def find_parent(parent, x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent, parent[x]) 
#   return parent[x]

# def union_parent(parent, x, y):
#   x = find_parent(parent, x)
#   y = find_parent(parent, y)
#   if x > y:
#     parent[x] = y
#   else:
#     parent[y] = x
    
# for _ in range(m):
#   a,b = map(int, sys.stdin.readline().split())
#   union_parent(parent,a, b)
    
# result = []
# for i in range(1,n+1):
#   data = find_parent(parent, i)
#   if data not in result:
#     result.append(data)
# print(len(result))

#필수 sys.setrecursionlimit(100000)
import sys 
sys.setrecursionlimit(100000)
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
visited = [False]*(n+1)
def dfs(n):
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      dfs(i)
      
def bfs(n):
  visited[n] = True
  q = [n]
  while q:
    now = q.pop(0)
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

count = 0
for i in range(1,n+1):
  if not visited[i]:
    # dfs(i)
    bfs(i)
    count += 1
print(count)
