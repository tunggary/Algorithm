import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
visited = [int(1e9)]*100001

def bfs(start):
  q = deque([start])
  visited[start] = 0
  
  while q:
    now = q.popleft()
    
    if now == K:
      print(visited[now])
      return
    
    for next, flag in [(2*now,True), (now+1,False), (now-1,False)]:
      if 0<=next<=100000:
        if flag:
          if visited[next] > visited[now]:
            visited[next] = visited[now]
            q.append(next)
        else:
          if visited[next] > visited[now]+1:
            visited[next] = visited[now]+1
            q.append(next)    
bfs(N)
