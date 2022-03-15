#백준 1764번

import sys
n,m = map(int, sys.stdin.readline().split())

not_sound = set()
not_watch = set()

for _ in range(n):
  not_sound.add(sys.stdin.readline().strip())
  
for _ in range(m):
  not_watch.add(sys.stdin.readline().strip())
  
intersection = not_sound & not_watch

print(len(intersection))
for ele in sorted(intersection):
  print(ele)