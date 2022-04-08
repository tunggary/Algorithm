#백준 16953번
#아이디어: bfs를 이용한 최단거리 구하기
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

def bfs():
  q = deque([(n,1)])
  while q:
    now, count = q.popleft()
    if now == m:
      print(count)
      return
    if now > m:
      continue
    else:
      q.append((now*10+1, count+1))
      q.append((now*2, count+1)) 
  print(-1)
  
bfs()