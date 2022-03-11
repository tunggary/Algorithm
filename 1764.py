# import sys
# n,m = map(int, input().split())
# data = dict()
# for i in range(n):
#   data[sys.stdin.readline().strip()] = i

# answer = []
# for i in range(m):
#   input = sys.stdin.readline().strip()
#   if data.get(input) != None:
#     answer.append(input)

# answer.sort()
# print(len(answer))
# for i in answer:
#   print(i)

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