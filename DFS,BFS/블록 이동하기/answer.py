#이코테 355p
#아이디어: 로봇이 갈 수 있는 곳을 파악하는 것이 중요

from collections import deque

def nextStep(graph, now):
    now = list(now)
    next = []
    l_x, l_y, r_x, r_y = now[0][0], now[0][1], now[1][0], now[1][1]
    steps = [(-1,0),(0,1),(1,0),(0,-1)]
    for step in steps:
        n_l_x = l_x + step[0]
        n_l_y = l_y + step[1]
        n_r_x = r_x + step[0]
        n_r_y = r_y + step[1]
        if graph[n_l_x][n_l_y] == 0 and graph[n_r_x][n_r_y] == 0:
            next.append({(n_l_x,n_l_y),(n_r_x,n_r_y)})
    if l_x == r_x:  
        for i in [-1,1]:
            if graph[l_x+i][l_y] == 0 and graph[r_x+i][r_y] == 0:
                next.append({(l_x,l_y),(l_x+i,l_y)})
                next.append({(r_x,r_y),(r_x+i,r_y)})
    if l_y == r_y:  
        for i in [-1,1]:
            if graph[l_x][l_y+i] == 0 and graph[r_x][r_y+i] == 0:
                next.append({(l_x,l_y),(l_x,l_y+i)})
                next.append({(r_x,r_y),(r_x,r_y+i)})
    return next
def solution(board):
    n = len(board)
    graph = [[1]*(n+2) for _ in range(n+2)]
    visited = []
    answer = 0
    for i in range(n):
        for j in range(n):
            graph[i+1][j+1] = board[i][j]

    q = deque()
    start = {(1,1), (1,2)}
    q.append((start, 0))
    visited.append(start)
    while q:
        now, cost = q.popleft()
        if (n,n) in now:
            answer = cost
            break
        for next_pos in nextStep(graph,now):
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)
    return answer
