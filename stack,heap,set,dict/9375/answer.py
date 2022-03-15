#백준 9375번
#아이디어: 옷의 종류 별로 그 종류의 옷을 입지 않는 하나의 경우를 더해서 곱한다. 그 중 아예 입지 않은 경우 한가지를 뺀다.

for _ in range(int(input())):
  n = int(input())
  clothes = dict()
  for i in range(n):
    a, b = input().split()
    if clothes.get(b) == None:
      clothes[b] = 1
    else:
      clothes[b] += 1
  
  answer = 1
  for i in clothes.values():
    answer *= (i+1)
  print(answer - 1)
