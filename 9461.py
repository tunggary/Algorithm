dp = [0]*101
dp[0] = dp[1] = dp[2] = 1
for i in range(3,101):
  dp[i] = dp[i-2] + dp[i-3]

for _ in range(int(input())):
  n = int(input())
  print(dp[n-1])
  