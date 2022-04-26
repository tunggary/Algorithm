import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N,E = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
for _ in range(E):
  a,b,w = map(int, input().split())
  graph[a].append((w,b))
  graph[b].append((w,a))
node1, node2 = map(int, input().split())

def dijkstra(start):
  distance = [INF]*(N+1)
  distance[start] = 0
  q = []
  heappush(q, (0,start))
  
  while q:
    dist, now = heappop(q)
    if distance[now] > dist:
      continue
    for i in graph[now]:
      cost = dist + i[0]
      if cost < distance[i[1]]:
        distance[i[1]] = cost
        heappush(q, (cost,i[1]))
  
  return distance

start = dijkstra(1)
startNode1 = dijkstra(node1)
startNode2 = dijkstra(node2)
count = min(start[node1]+startNode1[node2]+startNode2[N], start[node2]+startNode2[node1]+startNode1[N])
print( -1 if count >= INF else count)