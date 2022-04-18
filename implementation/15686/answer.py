#백준 15686번
#아이디어: 살아남을 치킨 집을 조합으로 구한다.

import sys
from itertools import combinations

N,M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
result = int(1e9)

for i in range(N):
  for j in range(N):
    if graph[i][j] == 2:
      chicken.append((i,j))
    elif graph[i][j] == 1:
      house.append((i,j))
  
for j in combinations(chicken, M):
  total = 0
  for hx,hy in house:
    min_value = int(1e9)
    for cx,cy in j:
      dist = abs(hx-cx) + abs(hy-cy)
      min_value = min(min_value, dist)
    total += min_value
  result = min(total, result)
    
print(result)