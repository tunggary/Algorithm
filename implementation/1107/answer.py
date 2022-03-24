#백준 1107번
#아이디어: 브루트포스 알고리즘으로 모든 경우를 체크해서 최소값을 찾는다.
#제한시간이 1초일때 O(N)의 시간복잡도 알고리즘은 10,000,000개 까지 가능함

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
brokenButton = list(sys.stdin.readline())
result = int(1e9)

def brokenCheck(number):
  numberList = list(str(number))
  for number in numberList:
    if number in brokenButton:
      return True
  return False
  
for i in range(1000000):
  if brokenCheck(i):
    continue
  result = min(result, len(str(i)) + abs(n-i))
result = min(result, abs(100-n))
print(result)