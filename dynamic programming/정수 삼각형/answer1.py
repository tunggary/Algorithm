#이코테 376p
#아이디어: 바텀업 방식으로 큰 값 체크

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
for row in range(1,n):
    for col in range(row+1):
        left_top = 0 if col == 0 else graph[row-1][col-1]
        right_top = 0 if col == row else graph[row-1][col] 
        graph[row][col] += max(left_top, right_top)

print(max(graph[n-1]))