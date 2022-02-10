#이코테 201p
#아이디어: 기준 떡의 길이를 이진탐색을 이용해 좁혀나간다.

n,h = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0

while start <= end:
  mid = (start + end)//2
  total = 0
  for i in data:
    if i > h:
      total += i - mid

  if total > h:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)
