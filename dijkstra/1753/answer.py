#백준 1753번
#아이디어: 다익스트라로 해결

import sys
from heapq import heappush, heappop

V,E = map(int, sys.stdin.readline().split())
INF = int(1e9)
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
  a,b,w = map(int, sys.stdin.readline().split())
  graph[a].append((b,w))
  

def dijkstra(start):
  q = []
  distance[start] = 0
  heappush(q,(0, start))
  
  while q:
    dist, now = heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        heappush(q,(cost, i[0]))
        distance[i[0]] = cost 
  
        
dijkstra(start)
for i in range(1,V+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])