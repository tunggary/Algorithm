#백준 2579번
import sys
n = int(sys.stdin.readline())
stairs = [0]
for _ in range(n):
  stairs.append(int(sys.stdin.readline()))
dp = [0]*(n+1)

if n == 1:
  print(stairs[1])
elif n == 2:
  print(stairs[1] + stairs[2])
else:
  dp[1] = stairs[1]
  dp[2] = stairs[1] + stairs[2]

  for i in range(3,n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])  
    
  print(dp[n])