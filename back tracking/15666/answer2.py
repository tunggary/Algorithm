#백준 15666번
#아이디어: 순차중복조합

import sys
from itertools import combinations_with_replacement

n,m = map(int, sys.stdin.readline().split())
number = sorted(map(int, sys.stdin.readline().split()))
result = {}

for i in combinations_with_replacement(number, m):
  if str(i) not in result:
    result[str(i)] = 1
    print(' '.join(map(str,i)))