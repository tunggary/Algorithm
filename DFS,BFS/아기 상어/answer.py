#이코테 402p
#아이디어: 완전 탐색을 활용한 구현문제

from collections import deque

n = int(input())
graph = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
INF = int(1e9)

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
#상어의 위치와 크기
now_x, now_y = 0, 0
now_size = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            #처음 상어의 위치 저장, 처음 위치의 물고기를 먹음
            now_x, now_y = i,j
            graph[i][j] = 0

#현재 위치에서 모든 맵까지의 최단거리를 완전탐색으로 구함         
def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

#모든 맵까지의 최단거리가 주어졌을때 가장 가깝고 먹을 수 있는 물고기 위치 구함
def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
                    
    if min_dist == INF:
        return None
    else:
        return [x,y,min_dist]
       
result = 0
ate = 0
      
while True:
    #다음 먹을 물고기 위치 구함
    value = find(bfs())
    if value == None:
        #없으면 결과 print
        print(result)
        break
    else:
        x,y,dist = value[0], value[1], value[2]
        graph[x][y] = 0
        now_x, now_y = x, y
        result += dist
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0