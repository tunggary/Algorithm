#백준 5525번
#아이디어: 반복되는 패턴을 이용하여 연속된 n개의 IOI를 구한다.
#시간 복잡도 O(N)을 만족하기 위해 반복문 한번에 모든걸 해결한다.

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

answer = 0
count = 0
i = 0

while i<m-2:
  if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
    count += 1
    if count == n:
      count -= 1
      answer += 1
    i+=1
  else:
    count = 0
  i+=1
  
print(answer)