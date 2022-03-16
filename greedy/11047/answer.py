#백준 11047번

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for i in range(n-1,-1,-1):
  count += k//coins[i]
  k %= coins[i]
print(count)