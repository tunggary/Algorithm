n,m,k = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
directions = list(map(int, input().split()))

smell = [[[0,0]]*n for _ in range(n)]

priorites = [[] for _ in range(m)]

for i in range(m):
    for j in range(4):
        priorites[i].append(list(map(int, input().split())))
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                
def move():
    new_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0:
                direction = directions[array[i][j]-1]
                param = False
                for index in range(4):
                    nx = i + dx[priorites[array[i][j]-1][direction-1][index]-1]
                    ny = j + dy[priorites[array[i][j]-1][direction-1][index]-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][1] == 0:
                            directions[array[i][j]-1] = priorites[array[i][j]-1][direction-1][index]
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[i][j]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[i][j])
                            param = True
                            break
                        
                if param:
                    continue
                
                for index in range(4):
                    nx = i + dx[priorites[array[i][j]-1][direction-1][index]-1]
                    ny = j + dy[priorites[array[i][j]-1][direction-1][index]-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][0] == array[i][j]:
                            directions[array[i][j]-1] = priorites[array[i][j]-1][direction-1][index]
                            new_array[nx][ny] = array[i][j]
                            break
    return new_array
time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1
    
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break