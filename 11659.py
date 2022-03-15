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