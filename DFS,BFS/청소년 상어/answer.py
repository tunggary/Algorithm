#이코테 404p
#아이디어: DFS를 이용하여 상어가 갈 수 있는 모든 경우의 수의 값중 최댓값을 구한다.

import copy

array = [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1]-1]
        
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
result = 0

def turn_left(direction):
    return (direction + 1) % 8

def find_fish(array, index):
    
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(1,17):
        position = find_fish(array, i)
        if position != None:
            x,y = position
            direction = array[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0<=nx<4 and 0<=ny<4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[nx][ny], array[x][y] = array[x][y], array[nx][ny]
                        break
                direction = turn_left(direction)
                
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for _ in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0<=now_x<4 and 0<=now_y<4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1
    
    move_all_fishes(array, now_x, now_y)
    
    positions = get_possible_positions(array, now_x, now_y)
    
    if len(positions) == 0:
        result = max(result, total)
        return
    else:
        for nx, ny in positions:
            dfs(array, nx, ny, total)
        
dfs(array, 0,0,0)
print(result)