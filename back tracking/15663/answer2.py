import sys
from itertools import permutations

n,m = map(int, sys.stdin.readline().split())
number = map(int, sys.stdin.readline().split())
          
for i in sorted(set(permutations(number, m))):
  print(' '.join(map(str,i)))