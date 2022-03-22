#백준 2108번
#아이디어: Counter를 이용한 최빈수 계산

import sys 
from collections import Counter

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]

data.sort()

def mode(nums):
  mode_dict = Counter(nums)
  modes = mode_dict.most_common()    
  
  if len(nums) > 1 : 
    if modes[0][1] == modes[1][1]:
      return modes[1][0]
  return modes[0][0]

print(round(sum(data)/n))
print(data[n//2])
print(mode(data))
print(data[-1]-data[0])