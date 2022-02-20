#이코테 341p
#아이디어: dfs를 이용하여 울타리 세우기

n,m = map(int,input().split())
graph = []
temp = [[0]*m for _ in range(n)]
steps = [(-1,0),(0,1),(1,0),(0,-1)]
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

def get_safe_zone():
    sum = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                sum += 1
    return sum

def spread_virus(x,y):
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread_virus(nx, ny)

def set_wall(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    spread_virus(i,j)
        result = max(result, get_safe_zone()) 
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                set_wall(count)
                graph[i][j] = 0
                count -= 1
    
set_wall(0)
print(result)
