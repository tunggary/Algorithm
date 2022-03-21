#백준 1697번
#아이디어: m까지 가는 최단 거리를 구하는 문제이므로 bfs의 원리를 이용하여 해결

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
visited = [0]*100001

def bfs(x):
  q = deque()
  q.append(x)
  
  while q:
    now = q.popleft()
    if now == m:
      print(visited[now])
      break
    for next in [now+1,now*2,now-1]:
      if 0 <= next <= 100000:
        if visited[next] == 0:
          visited[next] = visited[now] + 1
          q.append(next)
        
bfs(n)