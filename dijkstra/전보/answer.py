#이코테 262p

import heapq

n,m,start = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_instance = 0

for i in distance:
  if i != INF:
    count += 1
    max_instance = max(max_instance,i)

#시작 노드 빼야함
print(count-1,max_instance)
