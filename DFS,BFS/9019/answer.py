#백준 9019번
#아이디어: bfs를 이용한 최단거리 구하기 문제

import sys
from collections import deque

def getNext(now):
  D = (now*2)%10000
  S = (now-1)%10000
  L = (now//1000)+(now%1000)*10
  R = (now%10)*1000+(now//10)
  return [(D,"D"),(S,"S"),(L,"L"),(R,"R")]

def bfs(start, target):
  visited = [False]*10001
  q = deque([(start,"")])
  visited[start] = True
  
  while q:
    now, path = q.popleft()
    if now == target:
      print(path)
      break
    for next, oper in getNext(now):
      if not visited[next]:
        q.append((next, path+oper))
        visited[next] = True
    

for _ in range(int(sys.stdin.readline())):
  start, target = map(int, sys.stdin.readline().split())
  bfs(start,target)