#백준 16928번
#아이디어: bfs를 이용한 최단경로 구하기 문제

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
short_info = {}
visited = [-1]*101

for _ in range(n+m):
  start, end = map(int, sys.stdin.readline().split())
  short_info[start] = end
  
def check_next(current):
  next = short_info.get(current)
  if next == None:
    next = current
  return next
  
def bfs():
  q = deque([1])
  visited[1] = 0
  
  while q:
    now = q.popleft()
    for i in range(1,7):
      next = check_next(i + now)
      if 1<=next<=100 and visited[next] == -1:
        q.append(next)
        visited[next] = visited[now] + 1
bfs()
print(visited[100])