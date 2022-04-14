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
        if visited[now] + 1 <= visited[next]:
          q.append(next)
          visited[next] = visited[now] + 1
        
bfs(N)
print(visited[K])
print(result)