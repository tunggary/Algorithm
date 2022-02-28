#이코테 382p
#아이디어: 두 문자열의 유사도를 판별하는 알고리즘을 짜야함

from random import randrange


def edit(a,b):
    n = len(a)
    m = len(b)
    graph = [[0]*m for _ in range(n)]
    
    for i in range(n):
        graph[i][0] = i
        
    for i in range(m):
        graph[0][i] = i
        
    for i in range(1,n):
        for j in range(1,m):
            if a[i] == b[j]:
                graph[i][j] = graph[i-1][j-1]
            else:
                graph[i][j] = min(graph[i-1][j], graph[i-1][j-1], graph[i][j-1]) + 1
    
    return graph[n-1][m-1]
    
a = input()
b = input()

print(edit(a,b))