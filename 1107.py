import sys

n = sys.stdin.readline().strip()
m = int(sys.stdin.readline())
broken = sys.stdin.readline().split()

# result = ""
# for i in range(len(target)):
#   value = 10
#   click = 0
#   for button in range(10):
#     gap = abs(button - target[i])
#     if button not in broken and gap < value:
#       click = button
#       value = gap
#   result += str(click)

# answer = min(abs(100-n), abs(int(result)-n)+len(result))
# print(answer)

def check(str):
  for i in str:
    if i in broken:
      return False
  return True
  
result = int(1e9)
for i in range(1000001):
  if not check(str(i)):
    continue
  result = min(result, len(str(i)) + abs(i-int(n)))

print(min(result, abs(100-int(n))))
  