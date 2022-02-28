import heapq
# t = int(input())
steps = [(-1,0),(0,1),(1,0),(0,-1)]

def dijkstra(graph, start):
    n = len(graph)
    INF = int(1e9)
    x,y = start
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = graph[x][y]
    q = []
    heapq.heappush(q, (distance[x][y], (x,y)))
    
    while q:
        dist, now = heapq.heappop(q)
        x,y = now
        if dist > distance[x][y]:
            continue
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]        
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost,(nx,ny)))  
    print(distance[n-1][n-1])            
    
    
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dijkstra(graph, (0,0))
    