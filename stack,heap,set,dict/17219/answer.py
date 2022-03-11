#백준 17219번

import sys

n,m = map(int, sys.stdin.readline().split())
password = dict()
for _ in range(n):
  url, pw = sys.stdin.readline().strip().split()
  password[url] = pw
  
for _ in range(m):
  url = sys.stdin.readline().strip()
  print(password[url])