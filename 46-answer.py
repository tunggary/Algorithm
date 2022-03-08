from collections import deque

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
    
now_x, now_y = 0,0
now_size = 2
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[i][j] = 0
            
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist
        
def find(dist):
    x,y,min_dist = 0,0,int(1e9)
    for i in range(n):
        for j in range(n):
            if 1<= array[i][j] < now_size and dist[i][j] != -1:
                #왼쪽 상단 부터 이기 때문에 = 안넣음
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == int(1e9):
        return None
    else:
        return x,y,min_dist
    
result = 0
ate = 0
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0