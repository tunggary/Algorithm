#백준 13549번
#아이디어: bfs를 이용하여 최단거리를 구할때 순간이동은 0초가 걸리므로 현재 level과 같은 시간으로 처리되어야한다.

import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
visited = [int(1e9)]*100001

def bfs(start):
  visited[start] = 0
  q = deque([start])
  
  while q:
    now = q.popleft()
    if now == K:
      print(visited[now])
      return
    for next in [2*now, now+1, now-1]:
      if 0<=next<=100000:
        count = visited[now] + int(next != 2*now)
        if visited[next] >= count:
          visited[next] = count
          q.append(next)
            
bfs(N)