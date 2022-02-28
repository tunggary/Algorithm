#이코테 385p
#아이디어: 문제를 꼼꼼히 읽고, 플로이드 와샬 알고리즘 구현

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1): 
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j], end=" ")
    print()