import sys
from collections import deque
sys.setrecursionlimit(100000)

n,m = map(int, sys.stdin.readline().split())
visited = [0]*101
short = {}

for _ in range(n+m):
  start, end = map(int, sys.stdin.readline().split())
  short[start] = end
  
def check_short(current):
  next = short.get(current)
  if next == None:
    next = current
  return next

# def dfs(current, count):
#   global result
#   if current > 100:
#     return
#   elif current == 100:
#     result = min(result, count)
#   else:
#     current = check_short(current)
#     for i in range(1,7):
#       count += 1
#       dfs(current+i, count)
#       count -= 1
# dfs(1,0)

def bfs():
  q = deque([1])
  visited[1] = 0
  
  while q:
    now = q.popleft()
    for i in range(1,7):
      next = check_short(now + i)
      if 1 <= next <= 100 and visited[next] == 0:
        q.append(next)
        visited[next] = visited[now] + 1
          
bfs()
print(visited[100])