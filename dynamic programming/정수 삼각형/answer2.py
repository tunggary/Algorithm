#이코테 376p
#아이디어:  탑 다운 방식으로 큰 값 체크

n = int(input())
graph = []
memory = [[0]*(i+1) for i in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def dp(row,col):
    if row < 0 or col > row or col < 0:
        return 0
    if memory[row][col] != 0:
        return memory[row][col]
    
    left_top = dp(row-1, col-1)
    right_top = dp(row-1, col)
    memory[row][col] = graph[row][col] + max(left_top, right_top)
    
    return memory[row][col]

result = 0
for i in range(n):
    result = max(result, dp(n-1,i))
    
print(result)