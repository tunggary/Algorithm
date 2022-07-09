from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
print(tree)
result = 0

for _ in range(n-1):
  parent,child,cost = map(int, input().split())
  tree[parent].append((child, cost))
  
def dfs(n):
  global result
  if not tree[n]:
    return 0
  
  max_value = 0
  q = []
  heappush(q,0)
  for child, cost in tree[n]:
    value = dfs(child) + cost
    heappush(q, -value)
    max_value = max(value, max_value)
    
  first = -heappop(q)
  second = -heappop(q)  
  result = max(result, first+second)
  return max_value
  
dfs(1)
print(result)

# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
# n = int(input())
# tree = [[] for _ in range(n+1)]

# for _ in range(n-1):
#   a,b,cost = map(int, input().split())
#   tree[a].append((b,cost))
#   tree[b].append((a,cost))

# end_point = 0
# result = 0

# def dfs(n,cost,visited):
#   global end_point, result
#   if visited[n] == True:
#     return
#   visited[n] = True
  
#   if result < cost:
#     end_point = n
#     result = cost
    
#   for child, w in tree[n]:
#     dfs(child, cost+w,visited)

# dfs(1,0,[[False] for _ in range(n+1)])
# result = 0
# dfs(end_point,0,[[False] for _ in range(n+1)])
# print(result)
    