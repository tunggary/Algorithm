#이코테 113p
#아이디어: 시각의 전체 경우의 수는 24*60*60 이므로 10만을 넘지 않는다. 따라서 3중 for문으로 해결한다.

n = int(input())
result = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      # in 키워드를 사용하면 포함 여부를 알 수 있다.
      if '3' in str(i)+str(j)+str(k):
        result += 1

print(result)
