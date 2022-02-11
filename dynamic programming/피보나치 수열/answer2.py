#이코테 215p
#아이디어: 반복적(바텀업)

n = 100
d = [0]*(n+1)
d[1] = 1
d[2] = 1

for i in range(3,n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])
