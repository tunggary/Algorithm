#백준 11659번
#아이디어: 일반적인 방법으로 하면 시간초과가 나옴, 반복문을 적게 도는 방법을 생각해야함

import sys
n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sum = [data[0]]
for i in range(1, n):
  sum.append(data[i]+sum[i-1])

for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  if a <= 1:
    print(sum[b-1])
  else:
    print(sum[b-1] - sum[a-2]) 