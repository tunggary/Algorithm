import sys
from collections import deque

# def getNext(now):
#   D = str((int(now)*2)%10000).zfill(4)
#   S = "9999" if now == "0000" else str(int(now)-1).zfill(4)
#   L = now[1:4] + now[0]
#   R = now[3] + now[:3]
#   return [("D",D),("S",S),("L",L),("R",R)]
  
# def bfs(start, target, dp):
#   dp[int(start)] = ""
#   q = deque([start])
  
#   while q:
#     now = q.popleft()
#     if now == target:
#       print(dp[int(now)])
#       return
#     for next_info, next_num in getNext(now):
#       if dp[int(next_num)] == "":
#         dp[int(next_num)] = dp[int(now)] + next_info
#         q.append(next_num)
  
# for _ in range(int(sys.stdin.readline())):
#   start, target = sys.stdin.readline().split()
#   dp = [""]*10001  
#   bfs(start.zfill(4), target.zfill(4), dp)

def getNext(now):
  D = (2*now)%10000
  S = (now-1)%10000
  str_now = str(now).zfill(4)
  L = int(str_now[1:4]+str_now[0])
  R = int(str_now[3]+str_now[:3])
  return [(D,"D"),(S,"S"),(L,"L"),(R,"R")]

def bfs(start, target, visited):
  q = deque([(start, "")])
  visited[start] = True
  
  while q:
    now, path = q.popleft()
    if now == target:
      print(path)
      break
    for next, path_dir in getNext(now):
      if not visited[next]:
        visited[next] = True
        q.append((next, path+path_dir))

for _ in range(int(sys.stdin.readline())):
  start, target = map(int, sys.stdin.readline().split())
  visited = [False]*10001  
  bfs(start, target, visited)
