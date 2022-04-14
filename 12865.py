import sys

N,K = map(int, sys.stdin.readline().split())
stuffs = []
dp = [0]*(N+1)
result = 0
max_value = 0

for _ in range(N):
  W,V = map(int, sys.stdin.readline().split())
  stuffs.append((W,V))
  max_value = max(max_value, V)


def dfs(weight, value, count):
  global result
  
  if weight > K or count*max_value + value < result:
    return
  if stuffs:
    w,v = stuffs.pop()
    dfs(weight+w, value+v, count-1)
    dfs(weight, value, count-1)
    stuffs.append((w,v))
  else:
    result = max(result, value)
dfs(0,0,len(stuffs))
print(result)