import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)] #0:가로, 1:세로, 2:대각선
dp[0][1][0] = 1

for i in range(2,n):
  if graph[0][i] == 0:
    dp[0][i][0] = dp[0][i-1][0]

for i in range(1,n):
  for j in range(2,n):
    if graph[i][j] == 1:
      continue
    
    if graph[i-1][j-1] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
      dp[i][j][2] = sum(dp[i-1][j-1])
    dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
    dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
    
print(sum(dp[n-1][n-1]))