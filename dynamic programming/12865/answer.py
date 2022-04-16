#백준 12865번
#아이디어: 현재 물건을 넣을 수 있을때, 넣었을때랑 넣지 않았을때랑 가치 비교
#dp[i-1][j-weight] : 현재 i번째, 1,...,i-1번째 까지 물건을 넣을때 현재 넣을 수 있는 무게에서 i의 무게만큼 비워져 있을때 가치 최댓값

import sys

N,K = map(int, sys.stdin.readline().split())
stuffs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,K+1):
    weight = stuffs[i-1][0]
    value = stuffs[i-1][1]
    if j < weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
      
print(dp[N][K])
