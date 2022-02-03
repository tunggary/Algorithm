#거스름돈 문제
#손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
n = 1260
count = 0

array = [500, 100, 50, 10]

#O(K) K는 화폐의 종류
for coin in array:
  count += n // coin
  n %= coin

print(count)
