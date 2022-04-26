# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dp_max = [[0]*n for _ in range(n)]
# dp_min = [[0]*n for _ in range(n)]

# for i in range(n):
#   dp_max[0][i] = graph[0][i]
#   dp_min[0][i] = graph[0][i]
  
# for row in range(1,n):
#   for col in range(n):
#     if col == 0:
#       dp_max[row][col] = max(dp_max[row-1][col],dp_max[row-1][col+1])+graph[row][col]
#       dp_min[row][col] = min(dp_min[row-1][col],dp_min[row-1][col+1])+graph[row][col]
#     elif col == n-1:
#       dp_max[row][col] = max(dp_max[row-1][col],dp_max[row-1][col-1])+graph[row][col]
#       dp_min[row][col] = min(dp_min[row-1][col],dp_min[row-1][col-1])+graph[row][col]
#     else:
#       dp_max[row][col] = max(dp_max[row-1][col],dp_max[row-1][col+1],dp_max[row-1][col-1])+graph[row][col]
#       dp_min[row][col] = min(dp_min[row-1][col],dp_min[row-1][col+1],dp_min[row-1][col-1])+graph[row][col]

# print(max(dp_max[n-1]),min(dp_min[n-1]))

import sys
input = sys.stdin.readline

n = int(input())
dp_max_prev = [0]*3
dp_max_cur = [0]*3
dp_min_prev = [0]*3
dp_min_cur = [0]*3

for _ in range(n):
  col_0, col_1,col_2 = map(int, input().split())
  for col in range(3):
    if col == 0:
      dp_max_cur[col] = col_0 + max(dp_max_prev[0],dp_max_prev[1])
      dp_min_cur[col] = col_0 + min(dp_min_prev[0],dp_min_prev[1])
    elif col == 1:
      dp_max_cur[col] = col_1 + max(dp_max_prev[0],dp_max_prev[1],dp_max_prev[2])
      dp_min_cur[col] = col_1 + min(dp_min_prev[0],dp_min_prev[1],dp_min_prev[2])
    else:
      dp_max_cur[col] = col_2 + max(dp_max_prev[1],dp_max_prev[2])
      dp_min_cur[col] = col_2 + min(dp_min_prev[1],dp_min_prev[2])

  for col in range(3):
    dp_max_prev[col] = dp_max_cur[col]
    dp_min_prev[col] = dp_min_cur[col]
print(max(dp_max_prev), min(dp_min_prev)) 