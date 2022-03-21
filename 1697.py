import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
INF = int(1e9)
min_value = INF
dp = [INF]*100001

def bfs(x):
  global min_value
  q = deque()
  q.append((x,0))
  
  while q:
    now, count = q.popleft()
    if now == m:
      min_value = count
      break
    for i in range(3):
      if i == 0:
        next = now + 1
      elif i == 1:
        next = now * 2
      else:
        next = now - 1
      
      if 0 <= next <= 100000:
        if count+1 < dp[next]:
          q.append((next, count+1))
          dp[next] = count + 1
bfs(n)
print(min_value)
      
