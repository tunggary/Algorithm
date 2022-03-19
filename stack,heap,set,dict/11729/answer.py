#백준 11729번
#아이디어: 최소힙의 넣을때 -를 붙여서 최대힙으로 바꿔서 저장

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