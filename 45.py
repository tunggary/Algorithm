from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    teams = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(1, teams[i]):
            indegree[j] += 1
            graph[i+1].append(j)
    
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
        graph[b].remove(a)
        indegree[a] -= 1
        
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print()
    print(indegree, graph)
    
 