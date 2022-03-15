dp = [0]*12
# def dfs(n):
#   if dp[n] != 0:
#     return dp[n]
#   if n == 1:
#     return 1
#   if n == 2:
#     return 2
#   if n == 3:
#     return 4
#   dp[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)
#   return dp[n]

# for _ in range(int(input())):
#   n = int(input())
#   print(dfs(n))
  
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3,12):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
  
for _ in range(int(input())):
  n = int(input())
  print(dp[n-1])