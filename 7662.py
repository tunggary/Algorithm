# from collections import deque
# import sys

# for _ in range(int(sys.stdin.readline())):
#   n = int(sys.stdin.readline())
#   q = []
#   for _ in range(n):
#     command, num = sys.stdin.readline().split()
#     num = int(num)
#     if command == 'I':
#       q.append(num)
#       q.sort()
#     else:
#       if q:
#         if num == 1:
#           q.pop()
#         else:
#           q.pop(0)
#   if q:
#     print(q[-1], q[0])
#   else:
#     print('EMPTY')
      
from heapq import heappop, heappush
import sys

for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  max_heap = []
  min_heap = []
  all_exist = [False]*n
  
  for i in range(n):
    command, num = sys.stdin.readline().split()
    if command == 'I':
      heappush(min_heap,(int(num), i))
      heappush(max_heap,(-int(num), i))
      all_exist[i] = True
    else:
      if num == '1':
        while max_heap and not all_exist[max_heap[0][1]]:
          heappop(max_heap)
        if max_heap:
          all_exist[max_heap[0][1]] = False
          heappop(max_heap)
      else:
        while min_heap and not all_exist[min_heap[0][1]]:
          heappop(min_heap)
        if min_heap:
          all_exist[min_heap[0][1]] = False
          heappop(min_heap)
          
  while max_heap and not all_exist[max_heap[0][1]]:
    heappop(max_heap)
  while min_heap and not all_exist[min_heap[0][1]]:
    heappop(min_heap)
    
  if min_heap and max_heap:
    print(-max_heap[0][0], min_heap[0][0])
  else:
    print("EMPTY")