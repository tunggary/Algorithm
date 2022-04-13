#백준 1916번
#아이디어: 다익스트라

import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(m):
  a,b,w = map(int, sys.stdin.readline().split())
  graph[a].append((b,w))

departure, arrival = map(int, sys.stdin.readline().split())

def dijkstra(start):
  q = []
  heappush(q, (0, start))
  
  while q:
    dist, now = heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heappush(q,(cost, i[0]))
        
dijkstra(departure)
print(distance[arrival])