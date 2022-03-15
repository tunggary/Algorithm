
for _ in range(int(input())):
  n = int(input())
  clothes = dict()
  for _ in range(n):
    a,b = input().split()
    if clothes.get(b) != None:
      clothes[b] += 1
    else:
      clothes[b] = 1
  answer = 1
  for i in clothes.values():
    answer *= (i+1)

  print(answer-1)