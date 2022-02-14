#이코테 248p
#개선된 다익스트라 알고리즘: O(ElogV)

import heapq

n,m = map(int,input().split())
start = int(input())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

distance = [INF]*(n+1)

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  distance[start] = 0

  heapq.heappush(q,(0, start))
  
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])



  
