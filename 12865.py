# import sys

# N,K = map(int, sys.stdin.readline().split())
# stuffs = []
# dp = [0]*(N+1)
# result = 0
# max_value = 0

# for _ in range(N):
#   W,V = map(int, sys.stdin.readline().split())
#   stuffs.append((V/W,W,V))
#   max_value = max(max_value, V)
# stuffs.sort()

# def dfs(weight, value, count):
#   global result
  
#   if weight > K or count*max_value + value < result:
#     return
  
#   if stuffs:
#     a,w,v = stuffs.pop()
#     dfs(weight+w, value+v, count-1)
#     dfs(weight, value, count-1)
#     stuffs.append((a,w,v))
#   else:
#     print(value)
#     result = max(result, value)
  
# dfs(0,0,len(stuffs))
# print(result)


# import sys

# N,K = map(int, sys.stdin.readline().split())
# stuff = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# dp = [[0]*(K+1) for _ in range(N+1)]

# for i in range(1,N+1):
#   for j in range(1,K+1):
#     weight = stuff[i-1][0]
#     value = stuff[i-1][1]
#     if j < weight:
#       dp[i][j] = dp[i-1][j]
#     else:
#       dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

# print(dp[N][K])
  
  
  
import sys
sys.setrecursionlimit(1000000)

N,K = map(int ,sys.stdin.readline().split())
stuff = []
for _ in range(N):
  W,V = map(int, sys.stdin.readline().split())
  stuff.append((V/W, W, V))

stuff.sort(reverse=True)
stuff.insert(0,(0,0,0))

max_profit = 0
current = [0]*(N+1)

def promising(i,profit,weight):
  if weight >= K:
    return False
  else:
    j = i+1
    bound = profit
    total_weight = weight
    while j <= N and total_weight+stuff[j][1] <= K:
      total_weight += stuff[j][1]
      bound += stuff[j][2]
      j += 1
    if j <= N:
      bound += (K-total_weight)*(stuff[j][0])
  return bound > max_profit

def knapsack(i,profit, weight):
  global max_profit, current
  if weight <= K and profit > max_profit:
    max_profit = profit
  
  if promising(i,profit,weight):
    current[i+1] = 1
    knapsack(i+1, profit+stuff[i+1][2], weight+stuff[i+1][1])
    current[i+1] = 0
    knapsack(i+1, profit, weight)
    
knapsack(0,0,0)
print(max_profit)