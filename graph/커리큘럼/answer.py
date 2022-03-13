#이코테 303p
#아이디어: 위상정렬을 이용하여 풀이

from collections import deque

n = int(input())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)
result = [0]*(n+1)

for i in range(1,n+1):
  data = list(map(int, input().split()))
  time[i] = data[0]
  result[i] = data[0]
  for j in data[1:-1]:
    graph[j].append(i)
    indegree[i] += 1
  
q = deque()
for i in range(1,n+1):
  if indegree[i] == 0:
    q.append(i)
    
while q:
  now = q.popleft()
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      result[i] = max(result[i], result[now] + time[i])
      q.append(i)
      
for i in range(1,n+1):
  print(result[i])
      
