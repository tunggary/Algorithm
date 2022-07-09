from collections import deque


def solution(grid, k):
    answer = -1
    graph = [list(row) for row in grid]
    row, col = len(grid), len(grid[0])
    visited = [[[int(1e9)]*k for _ in range(col)] for _ in range(row)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[0][0][0] = 0
    q = deque([(0,0,0,0)])
    allPath = []
    
    while q:
        x,y,count,total = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if not graph[nx][ny] == '#' and count <= k and total < visited[nx][ny][]:
                    if graph[nx][ny] == '.':
                        q.append((nx,ny,0, total+1))
                        visited[nx][ny] = total + 1
                        
                    q.append((nx,ny,count+1, total+1))
                    visited[nx][ny] = total

    print(visited)
    print(allPath)
    
    return answer

solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)