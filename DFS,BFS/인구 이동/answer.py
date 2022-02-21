#이코테 353p
#아이디어: 완전탐색을 이용해 어떻게 인구 이동을 구할 것인가

from collections import deque
n, l, r = map(int, input().split())
graph = []
steps = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x,y):
    global n,r,l

    united = []
    united.append((x,y))
    sum = graph[x][y]
    count = 1
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for step in steps:
            nx = cx + step[0]
            ny = cy + step[1]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            gap = abs(graph[cx][cy]-graph[nx][ny])
            if not visited[nx][ny] and l <= gap <= r:
                queue.append((nx,ny))
                visited[nx][ny] = True
                united.append((nx,ny))
                sum += graph[nx][ny]
                count += 1
                
    for x,y in united:
        graph[x][y] = sum // count

total = 0
while True:
    visited = [[False]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
                index += 1
    if index == n*n:
        break
    total += 1
print(total)
