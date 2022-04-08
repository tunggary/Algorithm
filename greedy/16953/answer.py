#백준 16953번
#아이디어: 뒤에 숫자부터 보면서 하나씩 빼거나 2로 나눔

import sys
N,M = map(int, sys.stdin.readline().split())

result = 1
while True:
  if M == N:
    print(result)
    break
  elif M < N:
    print(-1)
    break
  
  if M % 10 == 1:
    M = M // 10
  elif M % 2 == 1:
    print(-1)
    break
  else:
    M = M // 2
  result += 1