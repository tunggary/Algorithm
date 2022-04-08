import sys

for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
  
  for i in range(1,n):
    if i==1:
      sticker[0][1] += sticker[1][0]
      sticker[1][1] += sticker[0][0]
    else:
      sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2]) 
      sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
  print(max(sticker[0][n-1], sticker[1][n-1]))