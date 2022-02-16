#이코테 315p
#정당성: 특정 무게의 공의 갯수를 구해서 무게별로 가질 수 있는 모든 경우의 수를 구한다.

n,m = map(int,input().split())
data = list(map(int,input().split()))
array = [0]*11
result = 0

for i in data:
  array[i] += 1

for i in range(1,m+1):
  n -= array[i]
  result += array[i]*n

print(result)
