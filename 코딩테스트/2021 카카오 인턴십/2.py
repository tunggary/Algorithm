steps = [(0,1),(0,2),(1,1),(1,0),(2,0),(1,-1),(0,-1),(0,-2),(-1,-1),(-1,0),(-2,0),(-1,1)]

def check(x:int, y:int, graph:list[list]):
    n = len(graph)
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 'P':
                if nx == x and abs(ny-y) >= 2:
                    if graph[nx][(y+ny)//2] == 'X':
                        continue
                    else:
                        return False
                elif ny == y and abs(nx-x) >= 2:
                    if graph[(x+nx)//2][ny] == 'X':
                        continue
                    else:
                        return False
                else:
                    if graph[nx][y] == 'X' and graph[x][ny] == 'X':
                        continue
                    else:
                        return False
    return True

def solution(places:list[list[str]]):
    answer = []
    for place in places:
        graph = [list(string) for string in place]
        n = len(graph)
        people = []
            
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'P':
                    people.append((i,j))
                    
        flag = True
        for x,y in people:
            if not check(x,y,graph):
                flag = False
                answer.append(0)
                break
        if flag:
            answer.append(1)
            
    return answer

print(solution([["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]]))