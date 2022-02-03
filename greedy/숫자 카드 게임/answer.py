#이코테 96p
#정당성 : 행의 가장 작은 값들 중에서 가장 큰 값을 찾으면 됨

n,m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  list_min = min(data)
  result = max(list_min,result)

print(result)
