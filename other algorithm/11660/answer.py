#백준 11660번
#아이디어: 구간합을 이용해서 답 구하기

import sys 

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    sum[i][j] = graph[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
    
for x1,y1,x2,y2 in result:
  print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])