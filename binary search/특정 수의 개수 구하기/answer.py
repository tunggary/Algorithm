#정열된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left,bisect_right

def count_by_range(a, left, right):
  l_index = bisect_left(a, left)
  r_index = bisect_right(a, right)
  return r_index - l_index

x = map(int, input().split())
data = list(map(int, input().split()))

result = bisect_right(data,x) - bisect_left(data, x)
if result == 0:
  result = -1
print(result)
