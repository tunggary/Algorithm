#백준 11286번
#아이디어: 힙을 이용하여 풀이

import sys
import heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
  x = int(sys.stdin.readline())
  if x != 0:
    heapq.heappush(q, (abs(x),x))
  else:
    if q:
      print(heapq.heappop(q)[1])
    else:
      print(0)