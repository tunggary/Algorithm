#이코테 351p
#아이디어 조합을 이용한 풀이

from itertools import combinations

def dfs(x,y,dir,temp):
    global n
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if temp[x][y] == 'O':
        return False
    elif temp[x][y] == 'S':
        return True
    else:
        return dfs(x+steps[dir][0], y+steps[dir][1], dir, temp)
    
n = int(input())
graph = []
temp = [['X']*n for _ in range(n)]
teachers = []
students = []
objects = []
steps = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(n):
    graph.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i,j))
        elif graph[i][j] == 'T':
            teachers.append((i,j))
        else:
            objects.append((i,j))

comb = list(combinations(objects, 3))
answer = 'NO'
for i in comb:
    for j in range(n):
        for k in range(n):
            temp[j][k] = graph[j][k]
    for x,y in i:
        temp[x][y] = 'O'
        
    count = 0
    for t_x, t_y in teachers:
        param1 = dfs(t_x,t_y,0, temp)
        param2 = dfs(t_x,t_y,1, temp)
        param3 = dfs(t_x,t_y,2, temp)
        param4 = dfs(t_x,t_y,3, temp)
        if not param1 and not param2 and not param3 and not param4:
            count += 1
    
    if count == len(teachers):
        answer = 'YES'
        break

print(answer)
