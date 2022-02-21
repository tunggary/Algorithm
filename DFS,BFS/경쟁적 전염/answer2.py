#이코테 344p
#아이디어: 큐에 원리(선입선출)를 이해하면 1초 동안만 퍼지고 다음 바이러스를 처리할 수 있음, 이는 앞에 내가 푼 풀이 보다 10배 가까이 빠르게 처리한다.

from collections import deque

n,k = map(int, input().split())
graph = []
virus = []
steps = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
s,x,y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],0,i,j))

virus.sort()
q = deque(virus)

while q:
    virus_num, second, target_x, target_y = q.popleft()
    if second == s:
        break
    for step in steps:
        nx = step[0] + target_x
        ny = step[1] + target_y
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                q.append((virus_num,second+1, nx, ny))
            
print(graph[x-1][y-1])
