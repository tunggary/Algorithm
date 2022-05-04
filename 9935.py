# import sys
# input = sys.stdin.readline

# original = input().strip()
# remove = input().strip()
# startPoint = 0
# mLen = len(remove)
# i = 0
# while i < len(original):
#   if original[i] == remove[0]:
#     startPoint = i
#     endPoint = i
#     while endPoint < len(original)-1 and original[endPoint] == original[endPoint+1]:
#       endPoint += 1
#     while endPoint >= startPoint:
#       if original[endPoint:endPoint+mLen] == remove:
#         if endPoint == 0:
#           original = original[mLen:]
#         else:
#           original = original[:endPoint]+original[endPoint+mLen:]
#       endPoint -= 1
#   else:
#     i+=1
    
# if len(original) == 0:
#   print("FRULA")
# else:
#   print(original)

import sys
input = sys.stdin.readline

original = input().strip()
remove = input().strip()

stack = []
lastChar = remove[-1]
length = len(remove)

for char in original:
  stack.append(char)
  if char == lastChar and remove == ''.join(stack[-length:]):
    del stack[-length:]
    
answer = ''.join(stack)
if answer == '':
  print("FRULA")
else:
  print(answer)
  