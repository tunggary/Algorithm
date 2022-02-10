#이코테 189p
#재귀 함수를 이용한 이진 탐색

def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end)//2
  if array[mid] == target: return mid
  elif array[mid] < target:
    return binary_search(array, target, mid + 1, end)
  else:
    return binary_search(array, target, start, mid - 1)
  
n, target = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = binary_search(data, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
