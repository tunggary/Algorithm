# import sys
# from collections import deque
# sys.setrecursionlimit(100000)

# n = int(sys.stdin.readline())
# graph = [[0]*n for _ in range(n)]

# dx = [0,1,1,1,0,-1,-1,-1]
# dy = [1,1,0,-1,-1,-1,0,1]
# nextStep = [(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
# result = 0

# def check(x,y, visited):
#   for i in range(8):
#     cx, cy = x, y
#     while True:
#       nx = cx + dx[i]
#       ny = cy + dy[i]
#       if nx<0 or nx>=n or ny<0 or ny>=n :
#         break
#       if (nx,ny) in visited:
#         return False
#       cx, cy = nx, ny
#   return True

# def bfs(x,y):
#   global n ,result
#   visited = [(x,y)]
#   q = deque([(x,y,1)])
  
#   while q:
#     cx, cy, count = q.popleft()
#     if count == n:
#       result += 1
#       continue
    
#     for i in nextStep:
#       nx = cx + i[0]
#       ny = cy + i[1]
#       if 0<=nx<n and 0<=ny<n:
#         if check(nx,ny,visited):
#           q.append((nx,ny,count+1))
#           visited.append((nx,ny))

# def dfs(x,y,visited):
#   global n,result
#   if len(visited) == n:
#     result += 1
#     return
#   for i in nextStep:
#     nx = x + i[0]
#     ny = y + i[1]
#     if 0<=nx<n and 0<=ny<n:
#       if check(nx,ny,visited):
#         visited.append((nx,ny))
#         dfs(nx,ny,visited)
#         visited.pop()
        
# for i in range(n):
#   for j in range(n):
#     dfs(i,j,[(i,j)])

# print(result)

# import sys

# N = int(sys.stdin.readline())
# result = 0
# row = [0]*N

# def check(n):
#   for i in range(n):
#     if row[i] == row[n] or abs(row[n] - row[i]) == n-i:
#       return False
#   return True

# def dfs(n):
#   global N, result
#   if n == N:
#     result += 1
#   else:
#     for i in range(N):
#       row[n] = i
#       if check(n):
#         dfs(n+1)
  
# dfs(0)
# print(result)

import sys 
n = int(sys.stdin.readline()) 
board = [0] * n 
ans_count = 0 
visited = [False] * n 

def check(x): 
    for i in range(x): 
        if abs(board[x] - board[i]) == x - i: 
            return False 
    return True 

def n_queen(x): 
    global ans_count 
    if x == n: 
        ans_count += 1 
        return 
    for i in range(n): 
        if visited[i]: 
            continue 
        board[x] = i 
        if check(x): 
            visited[i] = True 
            n_queen(x + 1) 
            visited[i] = False 
            
n_queen(0) 
print(ans_count)


  
