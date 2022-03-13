#백준 1463번
n = int(input())
INF = int(1e9)
dp = [0]*(1000001)
dp[1] = 0
dp[2] = 1
for i in range(2,n+1):
  min_value = INF
  if i % 3 == 0:
    min_value = min(min_value, dp[i//3]+1)
  if i % 2 == 0:
    min_value = min(min_value, dp[i//2]+1)
  min_value = min(min_value, dp[i-1]+1)
  dp[i] = min_value
  
print(dp[n])