# from sys import stdin

# def gcd(a,b):
#   if a%b == 0:
#     return b
#   else:
#     return gcd(b, a%b)
  
# def lcm(a,b):
#   return int(a*b/gcd(a,b))

# for _ in range(int(stdin.readline())):
#   m,n,x,y = map(int, stdin.readline().split())
#   year = lcm(m,n)
#   while year >= 1:
#     if year % m == x and year % n == y:
#       print(year)
#       break
#     year -= 1
#   if year == 0:
#     print(-1)

import sys

for _ in range(int(sys.stdin.readline())):
  m,n,x,y = map(int, sys.stdin.readline().split())
  param = True
  year = x
  while year <= m*n:
    if year%n == y%n:
      param = False
      print(year)
      break
    year += m
  
  if param:
    print(-1)
  
    