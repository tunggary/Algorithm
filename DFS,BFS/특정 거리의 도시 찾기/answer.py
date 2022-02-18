#이코테 339p
#아이디어: 모든 도로(간선)의 길이가 1이므로, bfs를 이용하여 풀 수 있다.

import sys
from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)

for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)

def bfs(start):
  distance[start] = 0
  q = deque([start])

  while q:
    now = q.popleft()
    for i in graph[now]:
      if distance[i] == -1:
        distance[i] = distance[now] + 1
        q.append(i)

bfs(x)

count = 0
for i in range(1,n+1):
  if distance[i] == k:
    print(i)
    count += 1
    
if count == 0:
  print(-1)

  
