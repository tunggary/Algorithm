#이코테 341p
#아이디어: 조합을 이용한 벽 세우기

import sys
from collections import deque
from itertools import combinations
import time

start_time = time.time()

n,m = map(int,input().split())
graph = []
graph_list = []
steps = [(-1,0),(0,1),(1,0),(0,-1)] #북 동 남 서
birus = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for row in range(n):
    for col in range(m):
        if graph[row][col] == 0:
            graph_list.append((row,col)) 
        if graph[row][col] == 2:
            birus.append((row,col))

#그래프에서 안전구역, 즉 0인 구역의 개수
def get_safe_area(map_info):
    global n,m
    sum = 0
    for row in range(n):
        for col in range(m):
            if map_info[row][col] == 0:
                sum += 1
    return sum

#바이러스가 퍼짐
def spread_birus(map_info):
    ret = map_info
    for i in birus:
        ret = bfs(ret,i)
    return ret

def bfs(map_info, start):
    global n,m
    q = deque()
    q.append(start)
    while q:
        row, col = q.popleft()
        for x,y in steps:
            n_row = row + x
            n_col = col + y
            if n_row < 0 or n_row >= n or n_col < 0 or n_col >= m:
                continue
            if map_info[n_row][n_col] == 0:
                
                map_info[n_row][n_col] = 2
                q.append((n_row,n_col))
    return map_info

comb = list(combinations(graph_list,3))
result = 0
temp = [[0]*m for _ in range(n)]
for info in comb:
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    for x,y in info:
        temp[x][y] = 1
    result = max(result, get_safe_area(spread_birus(temp)))
print(result)
