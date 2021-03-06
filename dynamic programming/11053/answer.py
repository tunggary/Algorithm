#백준 11053번
#아이디어: 가장 긴 증가하는 수열

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
result = [1]*(n)

for i in range(n):
  for j in range(0,i):
    if array[i] > array[j]:
      result[i] = max(result[i],result[j]+1)
      
print(max(result))
