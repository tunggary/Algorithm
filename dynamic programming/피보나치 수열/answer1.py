#이코테 212p
#아이디어: 재귀적 방식(탑다운)

d = [0]*100
def fibo(i):
  if i==1 or i==2:
    return 1
  if d[i] != 0:
    return d[i]
  d[i] = fibo(i-1) + fibo(i-2)
  return d[i]

print(fibo(10))
