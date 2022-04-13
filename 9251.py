# import sys

# str1 = sys.stdin.readline().strip()
# str2 = sys.stdin.readline().strip()
# n = len(str1)
# m = len(str2)

# i,j = 0,0
# count = 0
# while i<n and j<m:
#   if str1[i] == str2[j]:
#     i+=1
#     j+=1
#     count += 1
#   else:
#     i+=1
# while j<m:
#   if str1[i-1] == str2[j]:
#     count += 1
#   j+=1

# i,j = 0,0
# count2 = 0
# while i<n and j<m:
#   if str1[i] == str2[j]:
#     i+=1
#     j+=1
#     count2 += 1
#   else:
#     j+=1
# while i < n:
#   if str1[i] == str2[j-1]:
#     count2 += 1
#   i+=1
    
# print(max(count,count2))

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]
    
for i in range(1,n+1):
  for j in range(1,m+1):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
print(dp[n][m])