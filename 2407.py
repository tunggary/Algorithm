import sys

dp = [-1]*101

n,r = map(int,sys.stdin.readline().split())

def factorial(n):
  if dp[n] != -1:
    return dp[n]
  if n == 0:
    return 1
  dp[n] = n*factorial(n-1)
  return dp[n]

print(factorial(n)//(factorial(r)*factorial(n-r)))