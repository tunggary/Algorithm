import heapq

n,m = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
    
q = [(1,0)]
distance[1] = 0

while q:
    now, dist = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (i[0], cost))
 
result_value = 0
result_index = 0
result_count = 0           
for i in range(1,n+1):
    if result_value < distance[i]:
        result_index = i
        result_count = 1
        result_value = distance[i]
    elif result_value == distance[i]:
        result_count += 1

print(result_index, result_value, result_count)