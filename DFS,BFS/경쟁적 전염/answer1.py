#이코테 344p
#아이디어: 큐에 꺼내서 시간 초를 확인하고 탐색한다.
#경쟁적 전염
import sys

n,k = map(int, input().split())
graph = []
virus = [[] for _ in range(k+1)]
steps = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
s,x,y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i,j,0))
            
def bfs():
    global n,k,s,x,y
    for second in range(s):
        for i in range(1, k+1):            
            while True:
                if len(virus[i]) == 0:
                    break 
                if virus[i][0][2] != second:
                    break
                row, col, sec = virus[i].pop(0)
                for step in steps:
                    n_row = step[0] + row
                    n_col = step[1] + col
                    if 0<=n_row<n and 0<=n_col<n and graph[n_row][n_col] == 0:
                        graph[n_row][n_col] = i
                        virus[i].append((n_row, n_col, sec+1))
    print(graph[x-1][y-1])

bfs()
