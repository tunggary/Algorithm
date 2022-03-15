#백준 9095번
#bottom up 방식

dp = [0]*12
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3,12):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
  
for _ in range(int(input())):
  n = int(input())
  print(dp[n-1])