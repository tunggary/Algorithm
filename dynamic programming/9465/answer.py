#백준 9465번
#아이디어: dp를 사용할 때 현재를 기준으로 max값을 어떤 위치의 값들로 비교해야 하는지 잘 파악

import sys

input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]
  for i in range(1,n):
    if i==1:
      sticker[0][i] += sticker[1][0]
      sticker[1][i] += sticker[0][0]
    else:
      sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
      sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
  print(max(sticker[0][n-1], sticker[1][n-1]))