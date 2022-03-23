#백준 6064번
#아이디어: year를 한 기준 숫자(m,n) 만큼 더해나가면서 n으로 나눴을때 나머지 값을 (x,y)와 비교하면 됨

import sys

for _ in range(int(sys.stdin.readline())):
  m,n,x,y = map(int, sys.stdin.readline().split())
  year = x
  fail = True
  while year <= m*n:
    if year%n == y%n:
      fail = False
      break
    year += m
  if fail:
    print(-1)  
  else:
    print(year)