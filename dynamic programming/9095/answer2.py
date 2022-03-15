#백준 9095번
#top down 방식

dp = [0]*12
def dfs(n):
  if dp[n] != 0:
    return dp[n]
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  dp[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)
  return dp[n]

for _ in range(int(input())):
  n = int(input())
  print(dfs(n))