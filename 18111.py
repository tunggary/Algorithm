n,m,b = map(int, input().split())
graph = []
max_value = 0
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    max_value = max(max_value, max(data))
    
result_count = int(1e9)
result_value = 0
for i in range(max_value,-1, -1):
    bottom = 0
    top = 0
    for j in range(n):
        for k in range(m):
            if graph[j][k] < i:
                bottom += (i - graph[j][k])
            else:
                top += (graph[j][k] - i)
    
    inventory = b + top
    if inventory < bottom:
        continue
    count = 2*top + bottom
    if count < result_count:
        result_count = count
        result_value = i
print(result_count, result_value)