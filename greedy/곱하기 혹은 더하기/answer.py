#이코테 312p
#정당성 : 대부분의 경우 두 수를 +할 때보다 *할 때 수가 더 커진다. 단 두 수가 하나라도 0혹은 1이면 +할 때가 더 크다.

n = int(input())
result = int(string[0])

for i in range(1, len(string)):
  num = int(string[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
    
print(result)
