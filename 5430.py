import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
  commands = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline())
  array = sys.stdin.readline().strip()
  if len(array) > 2:
    array = deque(array[1:-1].split(','))
  else:
    array = deque()
  
  success = True
  direction = True
  for command in commands:
    if command == 'R':
      direction = not direction
    else:
      if array:
        if direction:
          array.popleft()
        else:
          array.pop()
      else:
        success = False
        break

  if success:
    if not direction:
      array.reverse()
    print('['+','.join(array)+']')
  else:
    print("error")