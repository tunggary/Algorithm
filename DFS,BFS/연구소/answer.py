#이코테 341p
#아이디어: 조합을 이용한 벽 세우기

from itertools import combinations
from collections import deque

n,m = map(int, input().split())
graph = [] #맵 정보
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = [[0]*m for _ in range(n)] #조합별로 맵을 저장하기 위한 용도의 맵
steps = [(-1,0),(0,1),(1,0),(0,-1)]
virus = [] #바이러스의 처음 위치
space = [] #빈 공간

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 0:
            space.append((i,j))

def spread_virus(temp):
    for v_x,v_y in virus:
        q = deque()
        q.append((v_x,v_y))

        while q:
            now = q.popleft()
            for step in steps:
                n_x = now[0] + step[0]
                n_y = now[1] + step[1]
                if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m:
                    continue
                if temp[n_x][n_y] == 0:
                    temp[n_x][n_y] = 2
                    q.append((n_x,n_y))
    return temp

def get_safe_zone(temp):
    global n,m
    sum = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                sum += 1
    return sum

comb = combinations(space, 3) #빈 공간에 벽을 세울 수 있는 3가지 경우의 수를 모두 뽑음
result = 0 #안전 공간의 개수
for li in comb:
    #맵 정보 초기화
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j] 
    #벽을 세움
    for w_x, w_y in li:
        temp[w_x][w_y] = 1
    #바이러스 퍼뜨림
    temp = spread_virus(temp)
    #안전구역의 갯수 구해서 큰 값을 저장
    result = max(result, get_safe_zone(temp))

print(result)

