#이코테 375p
#아이디어: 모든 원소까지 올 수 있는 최대값을 구하고 저장, 다른 원소가 최대값을 구할 때 사용할 수 있게함

count = int(input())

for _ in range(count):
    n,m = map(int, input().split())
    data = list(map(int, input().split()))
    index = 0
    graph = []
    #받아온 데이터 분리
    for i in range(n):
        graph.append(data[index: index+m])
        index += m
    
    #2번째 column 부터 마지막 column 까지 모든 행의 위치에서 올 수 있는 최대값을 계산 
    result = 0
    for col in range(1,m):
        for row in range(n):
            left_up = 0 if row == 0 else graph[row-1][col-1]  
            left_side = graph[row][col-1]
            left_down = 0 if row == n-1 else graph[row+1][col-1]
            graph[row][col] += max(left_up, left_side, left_down)
            if col == m-1:
                result = max(result, graph[row][col])
                
    print(result)