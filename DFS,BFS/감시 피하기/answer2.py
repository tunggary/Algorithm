#이코테 351p
#아이디어: DFS를 이용하여 벽을 세우는 방식

n = int(input())
graph = []
steps = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(n):
    graph.append(list(input().split()))

def watch(x,y):
    global n
    for step in steps:
        nx,ny = x,y
        while True:
            nx += step[0]
            ny += step[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if graph[nx][ny] == 'O':
                break
            if graph[nx][ny] == 'S':
                return True
    return False
    
def set_wall(count):
    if count == 3:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    if watch(i,j):
                        return 'NO'
        return 'YES'
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                if set_wall(count) == 'YES':
                    return 'YES'
                count -= 1
                graph[i][j] = 'X'
    return 'NO'

print(set_wall(0))
