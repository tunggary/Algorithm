#백준 7662번
#아이디어: heap 두개를 어떻게 동기화 시킬것인가가 중요

import sys
from heapq import heappush, heappop

for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  max_heap = []
  min_heap = []
  sync = [False]*(n+1)
  for i in range(n):
    command, num = sys.stdin.readline().split()
    if command == 'I':
      heappush(max_heap, (-int(num),i))
      heappush(min_heap, (int(num),i))
      sync[i] = True
    else:
      if num == '1':
        while max_heap and not sync[max_heap[0][1]]:
          heappop(max_heap)
        if max_heap:
          sync[max_heap[0][1]] = False
          heappop(max_heap)
      else:
          while min_heap and not sync[min_heap[0][1]]:
            heappop(min_heap)
          if min_heap:
            sync[min_heap[0][1]] = False
            heappop(min_heap)
  while max_heap and not sync[max_heap[0][1]]:
    heappop(max_heap)
  while min_heap and not sync[min_heap[0][1]]:
    heappop(min_heap)
  if max_heap and min_heap:
    print(-max_heap[0][0], min_heap[0][0])
  else:
    print("EMPTY")