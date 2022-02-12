#이코테 375p
#아이디어: 탑다운

n,m = map(int,input().split())
array = list(map(int,input().split()))
dp = []
index = 0
for i in range(n):
  dp.append(array[index: index+m])
  index += m

d = [[-1]*m for _ in range(n)]

def search(i,j):
  if j == 0:
    return dp[i][j]
  if d[i][j] != -1:
    return d[i][j]

  if i == 0:
    d[i][j] = dp[i][j]+max(search(i,j-1),search(i+1,j-1))
  elif i == n-1:
    d[i][j] = dp[i][j]+max(search(i,j-1),search(i-1,j-1))
  else:
    d[i][j] = dp[i][j]+max(search(i-1,j-1), search(i,j-1),search(i+1,j-1))
  return d[i][j]

result = 0
for i in range(n):
  result = max(result, search(i,m-1))
print(result)
