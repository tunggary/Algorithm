import sys
sys.setrecursionlimit(100000)
N,M = map(int, sys.stdin.readline().split())

# def dfs(n,count):
#   global N
#   if n == N:
#     print(count)
#     return
#   elif n < N:
#     print(-1)
#     return
    
#   if str(n)[-1] == '1':
#     dfs(n//10,count+1)
#   elif n % 2 == 0:
#     dfs(n//2,count+1)
#   else:
#     print(-1)
#     return
    
# dfs(M,1)

result = 1
while True:
  if M == N:
    print(result)
    break
  elif M < N:
    print(-1)
    break
  
  if M % 10 == 1:
    M = M // 10
  elif M % 2 == 1:
    print(-1)
    break
  else:
    M = M // 2
  result += 1