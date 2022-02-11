#이코테 220p
#아이디어: 탑다운

n = int(input())
data = list(map(int,input().split()))

d = [0]*n

def dp(i):
  if i == 0:
    return data[0]
  if i == 1:
    return max(data[0],data[1])
  if d[i] != 0:
    return d[i]

  d[i] = max(dp(i-1), dp(i-2)+data[i])
  return d[i]

print(dp(n-1))
