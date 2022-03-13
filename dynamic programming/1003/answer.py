#백준 1003번

dp0 = [0]*41
dp1 = [0]*41
def fibonachi0(n):
  if n == 0:
    return 1
  if n == 1:
    return 0
  if dp0[n] != 0:
    return dp0[n]
  
  dp0[n] = fibonachi0(n-1)+fibonachi0(n-2)
  return dp0[n]

def fibonachi1(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  if dp1[n] != 0:
    return dp1[n]
  
  dp1[n] = fibonachi1(n-1)+fibonachi1(n-2)
  return dp1[n]

for _ in range(int(input())):
  n = int(input())
  print(fibonachi0(n), fibonachi1(n))