# from collections import deque
# import sys

# input = sys.stdin.readline
# n,m = map(int, input().split())
# peopleKnow = list(map(int, input().split()))[1:]
# parties = [list(map(int, input().split()))[1:] for _ in range(m)]
# graph = [[] for _ in range(n+1)]
# people = [False]*(n+1)
# result = 0

# def bfs(i):
#   visited = [False]*(n+1)
#   visited[i] = True
#   people[i] = True
#   q = deque([i])
  
#   while q:
#     now = q.popleft()
#     for node in graph[now]:
#       if not visited[node]:
#         visited[node] = True
#         people[node] = True
#         q.append(node)

# for party in parties:
#   for i in range(len(party)-1):
#     graph[party[i]].append(party[i+1])
#     graph[party[i+1]].append(party[i])
    
# for i in peopleKnow:
#   bfs(i)
  
# for party in parties:
#   know = False
#   for i in party:
#     if people[i]:
#       know = True
#       break
#   if not know:
#     result += 1
  
# print(result)



#--------------------------------------
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
peopleKnow = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(m)]
result = [1]*m

for _ in range(m):
  for j in range(m):
    if parties[j] & peopleKnow:
      peopleKnow |= parties[j]
      result[j] = 0
  
print(sum(result))