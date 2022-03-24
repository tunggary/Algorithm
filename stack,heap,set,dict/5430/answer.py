#백준 5430번
#아이디어: 배열 뒤집는 것을 앞,뒤에서 pop하는 것으로 하기

from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
  commands = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline())
  inputList = sys.stdin.readline().strip()
  if n == 0:
    inputList = deque()
  else:
    inputList = deque(inputList[1:-1].split(","))
  reverse = False
  error = False

  for command in commands:
    if command == 'R':
      reverse = not reverse
    else:
      if inputList:
        if reverse:
          inputList.pop()
        else:
          inputList.popleft()
      else:
        error = True
        break
  
  if error:
    print("error")
  else:
    if reverse:
      inputList.reverse()
    print("["+','.join(inputList)+"]")