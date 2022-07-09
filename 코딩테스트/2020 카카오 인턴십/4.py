
from collections import deque

dir = [(1,0,0), (0,-1,1), (-1,0,2), (0,1,3)] #남,동,북,서

def bfs(board):
    N = len(board)
    q = deque()
    visited = [[[int(1e9)]*N for _ in range(N)] for _ in range(4)]

    for i in range(4):
        visited[i][0][0] = 0
    if board[1][0] != 1:
        visited[0][1][0] = 100
        q.append((1,0,0))
    if board[0][1] != 1:
        visited[3][0][1] = 100
        q.append((0,1,3))

    while q:
        x,y,prevDir = q.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0<=nx<N and 0<=ny<N:
                cost = 100 if prevDir == i else 600
                if board[nx][ny] == 0 and visited[prevDir][x][y] + cost <= visited[i][nx][ny]:                        
                    visited[i][nx][ny] =  visited[prevDir][x][y] + cost
                    q.append((nx,ny,i))
    return min(visited[0][N-1][N-1],visited[1][N-1][N-1],visited[2][N-1][N-1],visited[3][N-1][N-1])

def solution(board):    
    return bfs(board)
