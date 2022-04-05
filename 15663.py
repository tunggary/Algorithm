# not in 연산이 시간을 굉장히 많이 잡아먹음 dict연산으로 시간을 줄이자

import sys
from itertools import permutations
# n,m = map(int, sys.stdin.readline().split())
# number = sorted(map(int, sys.stdin.readline().split()))
# count = [0]*(10001)
# for i in number:
#   count[i] += 1
# result = {}
# array = []

# def dfs():
#   if len(array) == m:
#     string = ' '.join(map(str, array))
#     if not result.get(string):
#       print(string)
#       result[string] = 1
#     return
  
#   for i in number:
#     if count[i] > 0:
#       array.append(i)
#       count[i] -= 1
#       dfs()
#       count[i] += 1
#       array.pop()
      
# dfs()

n,m = map(int, sys.stdin.readline().split())
number = sorted(map(int, sys.stdin.readline().split()))
result = {}
          
for i in permutations(number, m):
  string = ' '.join(map(str, i))
  if not result.get(string):
    print(string)
    result[string] = 1