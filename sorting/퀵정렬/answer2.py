#퀵 정렬의 원리를 이용한 다른 풀이

arr = [5,6,3,7,4,2,1]

def quick(arr):
  if len(arr) <= 1: return arr
  pivot = arr[0]
  tail = arr[1:]
  
  #pivot 보다 작은 값들을 모아놓은 리스트
  left_side = [i for i in tail if i <= pivot]
  
  #pivot 보다 큰 값들을 모아놓은 리스트
  right_side = [i for i in tail if i > pivot]

  return quick(left_side) + [pivot] + quick(right_side)

print(quick(arr))
