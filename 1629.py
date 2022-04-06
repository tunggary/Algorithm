import sys

a,b,c = map(int, sys.stdin.readline().split())

def power(a,n):
  if n == 0:
    return 1
  x = power(a,n//2)
  if n%2 == 0:
    return (x*x)%c
  else:
    return (x*x*a)%c

print(power(a,b))