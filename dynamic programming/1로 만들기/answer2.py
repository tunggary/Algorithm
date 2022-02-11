#이코테 217p
#아이디어: 탑다운

x = int(input())
d = [0]*30001

def dp(i):
  if i == 1:
    return 0
  if d[i] != 0:
    return d[i]

  d[i] = dp(i-1)+1
  if i % 2 == 0:
    d[i] = min(d[i],dp(i//2)+1)
  if i % 3 == 0:
    d[i] = min(d[i],dp(i//3)+1)
  if i % 5 == 0:
    d[i] = min(d[i],dp(i//5)+1)
  return d[i]

print(dp(x))
