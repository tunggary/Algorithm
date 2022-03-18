import heapq
import sys
n = int(sys.stdin.readline())

q = []
for _ in range(n):
  input = int(sys.stdin.readline())
  if input == 0:
    if q:
      print(-heapq.heappop(q))
    else:
      print(0)
  else:
    heapq.heappush(q, -input)