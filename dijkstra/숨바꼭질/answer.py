#이코테 40번
#아이디어: 다익스트라 알고리즘을 이용하여 최단 경로를 구하면 됨

import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1,b))
    graph[b].append((1,a))

distance[1] = 0
q = []
heapq.heappush(q, (distance[1], 1))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[0]
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

result_index = 0
result_value = 0
result_count = 0
for i in range(1, n+1):
    if distance[i] > result_value:
        result_value = distance[i]
        result_index = i
        result_count = 1
    elif distance[i] == result_value:
        result_count += 1
        
print(result_index, result_value, result_count)
    