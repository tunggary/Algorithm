count = int(input())

for _ in range(count):
    n,m = map(int, input().split())
    data = list(map(int, input().split()))
    index = 0
    graph = []
    result = 0
    for i in range(n):
        graph.append(data[index: index+m])
        index += m
    for col in range(1,m):
        for row in range(n):
            left_up = 0 if row == 0 else graph[row-1][col-1]  
            left_side = graph[row][col-1]
            left_down = 0 if row == n-1 else graph[row+1][col-1]
            graph[row][col] += max(left_up, left_side, left_down)
            if col == m-1:
                result = max(result, graph[row][col])
    print(result)