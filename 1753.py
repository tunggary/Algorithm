import sys
from heapq import heappop, heappush

V,E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
INF = int(1e9)
distance = [INF]*(V+1)

for _ in range(E):
  u,v,w = map(int, sys.stdin.readline().split())
  graph[u].append((v,w))
  
def dijkstra(start):
  distance[start] = 0
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
        
dijkstra(start)

for i in distance[1:]:
  if i == INF:
    print("INF")
  else:
    print(i)