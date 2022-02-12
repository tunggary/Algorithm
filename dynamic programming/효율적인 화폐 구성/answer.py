#이코테 226p
#아이디어: 그리디 알고리즘에서 다루었던 거스름 돈 문제랑 다름. 항상 화폐의 큰 단위가 작은 단위의 배수가 아닐 수 있기 때문에 다이나믹 프로그래밍으로 문제를 해결해야함
#점화식: a(i) = 금액 i를 만들 수 있는 최소한의 화폐 개수, k = 각 화폐의 단위, 각 화폐의 단위인 k를 하나씩 확인하며 
#a(i-k)를 만드는 방법이 존재하는 경우, a(i) = min(a(i),a(i-k)+1)
#a(i-k)를 만드는 방법이 존재하지 않는 경우, a(i) = INF

money = []
for i in range(n):
  money.append(int(input()))

d = [10001]*(m+1)
d[0] = 0

for i in range(n):
  for j in range(money[i], m+1):
    if d[j-money[i]] != 10001:
      d[j] = min(d[j], d[j - money[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
