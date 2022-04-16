#백준 12851번
#아이디어: bfs는 특정위치까지 최단경로를 구해준다. 즉 그 위치에 가장 먼저 입력되는 값이 
#최솟값이다. 그 후에 들어오는 값은 최솟값보다 같거나 큰데 이 문제에서는 같은 값들의 갯수를 모두 구해야하므로 방문 조건에 등호를 추가한다.

import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
visited = [int(1e9)]*100001
result = 0

def bfs(start):
  global result
    
  visited[start] = 0
  q = deque([start])
  
  while q:
    now = q.popleft()
    if now == K:
      result += 1
      continue
    for next in [2*now, now+1, now-1]:
      if 0<=next<=100000:
        #방문 조건에 등호 추가
        if visited[now] + 1 <= visited[next]:
          q.append(next)
          visited[next] = visited[now] + 1
        
bfs(N)
print(visited[K])
print(result)