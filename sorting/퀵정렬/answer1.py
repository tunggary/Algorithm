#이코테 164p
#퀵정렬: pivot(기준 데이터)를 설정하고 pivot보다 작은 데이터는 왼쪽에 큰 데이터는 오른쪽에 배치

arr = [5,6,3,7,4,2,1]

def quick(start, end, arr):
  if start >= end : 
    return
  pivot = start
  left = start + 1
  right = end 

  while left <= right:
    while left <= end and arr[pivot] >= arr[left]:
      left += 1
    while right > start and arr[pivot] <= arr[right]:
      right -= 1
    if left > right:
      arr[right],arr[pivot] = arr[pivot], arr[right]
    else:
      arr[right],arr[left] = arr[left], arr[right]

  quick(start,right-1, arr)
  quick(right+1, end, arr)

quick(0, len(arr)-1, arr)
print(arr)
