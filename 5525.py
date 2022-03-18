# n = int(input())
# m = int(input())
# nString = "I"
# mString = input()
# for i in range(n):
#   nString += 'OI'
    
# count = 0
# for i in range(m-(2*n)):
#   if mString[i:i+2*n+1] == nString:
#     count += 1
    
# print(count)

# n = int(input())
# m = int(input())
# mString = input()

# i,j = 0,1
# iCount, jCount = 0,0
# result = []
# while i<m-2 or j<m-2:
#   if i < m-2:
#     if mString[i] == 'I' and mString[i+1] == 'O' and mString[i+2] == 'I':
#       iCount += 1
#     else:
#       if iCount - n >= 0:
#         result.append(iCount - n + 1)
#       iCount = 0
      
#   if j < m-2:
#     if mString[j] == 'I' and mString[j+1] == 'O' and mString[j+2] == 'I':
#       jCount += 1
#     else:
#       if jCount - n >= 0:
#         result.append(jCount - n + 1)
#       jCount = 0
#   i+=2
#   j+=2
# if iCount > 0:
#   if iCount - n >= 0:
#     result.append(iCount - n + 1)
# if jCount > 0:
#   if jCount - n >= 0:
#     result.append(jCount - n + 1)
# print(sum(result))

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