#이코테 314p
#정당성: 화폐를 오름차순으로 정렬하고 만들 수 있는 금액에 차례대로 더한 값이 다음 단위보다 작을 경우 만들 수 없는 금액이 나온다.

n = int(input())
money = list(map(int, input().split()))

money.sort()
result = 1

for i in money:  
  if i > result:
    break
  result += i

print(result)
