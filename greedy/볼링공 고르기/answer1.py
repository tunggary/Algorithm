#이코테 315p
#정당성: 공을 2개 선택할 수 있는 모든 경우의 수 확인

n,m = map(int,input().split())
data = list(map(int,input().split()))
count = 0
for i in range(len(data)):
  for j in range(i,len(data)):
    if data[i] != data[j]:
      count += 1

print(count)
