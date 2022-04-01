import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())
for i in combinations(range(1,n+1),m):
  print(' '.join(map(str,i)))

print()