#이코테 92p
#정당성 : 가장 큰 수를 k번 더하고 두번째로 큰 수를 한번 더하는 것을 반복하면 가장 큰 수를 얻을 수 있다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

count_k = 0
result = 0

data.sort(reverse = True)

for i in range(m):
  if count_k < k:
    result += data[0]
    count_k += 1
  else:
    result += data[1]
    count_k = 0

print(result)
