# from collections import deque

# n,m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# indegree = [0]*(n+1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     indegree[b] += 1

# print(graph, indegree)
# q = deque()
# for i in range(1,n+1):
#     if indegree[i] == 0:
#         q.append(i)

# while q:
#     now = q.popleft()
#     print(now)
#     for i in graph[now]:
#         indegree[i] -= 1
#         if indegree[i] == 0:
#             q.append(i)

from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
indegree = [0]*(n+1)
outdegree = [0]*(n+1)

def bfs(start):
    global n
    visited = [False] * (n+1)
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:          
                visited[i] = True
                outdegree[start] += 1
                indegree[i] += 1
                q.append(i)
for i in range(1,n+1):
    bfs(i)

result = 0
for i in range(1,n+1):
    if indegree[i]+outdegree[i] == n-1:
        result += 1
        
print(result)