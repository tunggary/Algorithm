#백준 1931번
#아이디어: 끝나는 시간이 빠를 수록 더 많은 회의를 진행할 수 있다. 
#시작 시간과 끝나는 시간이 같은 회의가 들어올 수 있으므로 이 경우도 모두 포함하기 위해서 시작시간이 빠른 회의부터 체크를 한다.

import sys
n = int(sys.stdin.readline())
times = []
for _ in range(n):
  start, end = map(int, sys.stdin.readline().split())
  times.append((start, end))
  
times.sort(key=lambda x: (x[1], x[0]))

last = 0
count = 0
for start, end in times:
  if last <= start:
    count += 1
    last = end
    
print(count)
        