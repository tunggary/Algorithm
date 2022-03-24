# from copy import deepcopy
# import sys

# m,n,h = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(h)]
# for i in range(h):
#   for j in range(n):
#     graph[i].append(list(map(int, sys.stdin.readline().split())))
  
# dx = [0,1,0,-1,0,0]
# dy = [1,0,-1,0,0,0]
# dz = [0,0,0,0,1,-1]

# def spread(z,x,y,array):
#   global n,m,h
#   for i in range(6):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     nz = z + dz[i]
#     if 0<=nx<n and 0<=ny<m and 0<=nz<h:
#       if graph[nz][nx][ny] == 0:
#         array[nz][nx][ny] = 1
        
# def check(array):
#   global n,m,h
#   for z in range(h):
#     for x in range(n):
#       for y in range(m):
#         if array[z][x][y] == 0:
#           return False
#   return True  
        
# for z in range(h):
#   for x in range(n):
#     for y in range(m):
#       if graph[z][x][y] == 0:
#         count = 0
#         for i in range(6):
#           nx = x + dx[i]
#           ny = y + dy[i]
#           nz = z + dz[i]
#           if 0<=nx<n and 0<=ny<m and 0<=nz<h:
#             if graph[nz][nx][ny] == -1:
#               count += 1
#           else:
#             count += 1
#         if count == 6:
#           print(-1)
#           exit(0)
  
# result = 0
# while True:
#   array = deepcopy(graph)
#   if check(array):
#     break
#   for i in range(h):
#     for j in range(n):
#       for k in range(m):
#         if graph[i][j][k] == 1:
#           spread(i,j,k,array)
#   graph = array
#   result += 1
# print(result)
      
      
import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
  
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

def check():
  value = 0
  for z in range(h):
    for x in range(n):
      for y in range(m):
        if graph[z][x][y] == 0:
          return -1
        value = max(value, graph[z][x][y])
  return value - 1
  

def bfs():
  while q:
    cx,cy,cz = q.popleft()
    for i in range(6):
      nx = cx + dx[i]
      ny = cy + dy[i]
      nz = cz + dz[i]
      if 0<=nx<n and 0<=ny<m and 0<=nz<h:
        if graph[nz][nx][ny] == 0 or graph[nz][nx][ny] > graph[cz][cx][cy] + 1:
          q.append((nx,ny,nz))
          graph[nz][nx][ny] = graph[cz][cx][cy] + 1

for z in range(h):
  for x in range(n):
    for y in range(m):
      if graph[z][x][y] == 1:
        q.append((x,y,z))
bfs()

print(check())
