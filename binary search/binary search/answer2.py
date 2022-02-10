#이코테 190p
#반복문을 이용한 이진탐색

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return None
  
n, target = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = binary_search(data, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
