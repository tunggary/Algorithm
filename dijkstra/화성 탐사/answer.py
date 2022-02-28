#이코테 388p
#아이디어: 다익스트라 알고리즘 활용
import heapq
t = int(input())
INF = int(1e9)
steps = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(t):
    n = int(input())
    distance = [[INF]*n for _ in range(n)]
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    q = []
    distance[0][0] = graph[0][0]
    heapq.heappush(q, (distance[0][0],0,0))

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
