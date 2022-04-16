#백준 13549번
#아이디어: bfs를 이용하여 최단거리를 구할때 순간이동은 0초가 걸리므로 현재 level과 같은 시간으로 처리되어야한다.

import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
visited = [False]*100001

def bfs(start):
  visited[start] = True
  q = deque([(start,0)])
  
  while q:
    now, count = q.popleft()
    if now == K:
      print(count)
      return
    for next in [2*now, now+1, now-1]:
      if 0<=next<=100000:
        if not visited[next]:
          visited[next] = True
          if next == 2*now:
            q.appendleft((next, count))
          else:
            q.append((next,count+1))
            
bfs(N)